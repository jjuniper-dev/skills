"""
Neo4j Graph Query Builder
Helper functions for common graph queries and patterns
"""

from typing import List, Dict, Any, Optional, Tuple
from neo4j import Driver, Session
import logging

logger = logging.getLogger(__name__)


class GraphQueryBuilder:
    """Build and execute common Neo4j queries"""

    def __init__(self, driver: Driver):
        """
        Initialize with Neo4j driver

        Args:
            driver: Neo4j Driver instance
        """
        self.driver = driver

    def get_organizational_hierarchy(
        self,
        person_id: str,
        max_depth: int = 5
    ) -> Dict[str, Any]:
        """
        Get organizational hierarchy for a person (reports, team, org structure)

        Args:
            person_id: ID of the person
            max_depth: Max depth to traverse

        Returns:
            Dictionary with person info and hierarchical relationships
        """
        query = """
        MATCH (person:Person {id: $person_id})

        OPTIONAL MATCH (person)-[:REPORTS_TO*0..depth]->(manager:Person)
        WITH person, manager, depth

        OPTIONAL MATCH (person)-[:MEMBER_OF]->(team:Team)
        OPTIONAL MATCH (team)-[:LEADS*0..1]->(parent_team:Team)
        OPTIONAL MATCH (team)<-[:MEMBER_OF]-(teammate:Person)

        RETURN {
            person: {
                id: person.id,
                name: person.name,
                email: person.email,
                role: person.role
            },
            reportsTo: CASE WHEN manager IS NOT NULL THEN {
                id: manager.id,
                name: manager.name,
                role: manager.role
            } ELSE null END,
            team: CASE WHEN team IS NOT NULL THEN {
                id: team.id,
                name: team.name
            } ELSE null END,
            parentTeam: CASE WHEN parent_team IS NOT NULL THEN {
                id: parent_team.id,
                name: parent_team.name
            } ELSE null END,
            teammates: collect({
                id: teammate.id,
                name: teammate.name,
                role: teammate.role
            })
        } as hierarchy
        """

        with self.driver.session() as session:
            result = session.run(query, person_id=person_id, depth=max_depth)
            return result.single()['hierarchy']

    def find_team_skill_gaps(
        self,
        team_id: str,
        required_skills: List[str]
    ) -> Dict[str, Any]:
        """
        Find skill gaps in a team

        Args:
            team_id: ID of the team
            required_skills: List of required skill names

        Returns:
            Dictionary with coverage analysis
        """
        query = """
        MATCH (team:Team {id: $team_id})
        MATCH (team)<-[:MEMBER_OF]-(person:Person)

        WITH team, person, $required_skills as required_skills

        OPTIONAL MATCH (person)-[:HAS_SKILL]->(skill:Skill)
        WHERE skill.name IN required_skills

        WITH team, required_skills,
             collect(DISTINCT skill.name) as covered_skills,
             collect(DISTINCT {
                 person: person.name,
                 skills: collect(skill.name)
             }) as team_members

        WITH required_skills, covered_skills, team_members,
             [s IN required_skills WHERE NOT s IN covered_skills] as gaps

        RETURN {
            requiredSkills: required_skills,
            coveredSkills: covered_skills,
            gaps: gaps,
            gapCount: size(gaps),
            coverage: size(covered_skills) * 100.0 / size(required_skills),
            teamMembers: team_members
        } as analysis
        """

        with self.driver.session() as session:
            result = session.run(
                query,
                team_id=team_id,
                required_skills=required_skills
            )
            return result.single()['analysis']

    def get_service_dependency_tree(
        self,
        service_id: str,
        max_depth: int = 3
    ) -> List[Dict[str, Any]]:
        """
        Get dependency tree for a service

        Args:
            service_id: ID of the service
            max_depth: Maximum recursion depth

        Returns:
            List of dependencies with tree structure
        """
        query = """
        MATCH (service:Service {id: $service_id})
        CALL apoc.path.expand(
            service,
            'DEPENDS_ON>',
            '-DEPENDS_ON',
            0,
            $max_depth
        ) YIELD path, relationships

        WITH nodes(path) as nodes
        RETURN {
            service: nodes[0].name,
            dependencies: [
                {
                    name: n.name,
                    tech_stack: n.tech_stack,
                    level: length(filter(x in nodes WHERE x = n)) - 1
                }
                for n in nodes[1..]
            ],
            depth: length(nodes) - 1
        } as tree
        """

        with self.driver.session() as session:
            result = session.run(
                query,
                service_id=service_id,
                max_depth=max_depth
            )
            records = [r['tree'] for r in result]
            return records

    def find_circular_dependencies(self) -> List[Tuple[str, str]]:
        """
        Find circular dependencies in service graph

        Returns:
            List of service pairs that form cycles
        """
        query = """
        MATCH (s1:Service)-[:DEPENDS_ON*2..]->(s1)
        RETURN DISTINCT s1.id as service_id, s1.name as service_name
        """

        with self.driver.session() as session:
            result = session.run(query)
            cycles = [r['service_name'] for r in result]
            return cycles

    def get_cross_team_dependencies(self) -> List[Dict[str, Any]]:
        """
        Find dependencies between teams (via services)

        Returns:
            List of team-to-team dependencies
        """
        query = """
        MATCH (t1:Team)-[:OWNS]->(s1:Service)-[:DEPENDS_ON]->(s2:Service)<-[:OWNS]-(t2:Team)
        WHERE t1.id <> t2.id
        RETURN {
            fromTeam: t1.name,
            toTeam: t2.name,
            services: collect(DISTINCT {
                from: s1.name,
                to: s2.name
            }),
            dependencyCount: count(DISTINCT s1)
        } as dependency
        ORDER BY dependency.dependencyCount DESC
        """

        with self.driver.session() as session:
            result = session.run(query)
            return [r['dependency'] for r in result]

    def recommend_service_owner(
        self,
        service_id: str
    ) -> Optional[Dict[str, Any]]:
        """
        Recommend person to own/maintain a service

        Args:
            service_id: ID of the service

        Returns:
            Person with highest expertise for the service
        """
        query = """
        MATCH (service:Service {id: $service_id})

        WITH service
        OPTIONAL MATCH (service)<-[:DEPENDS_ON]-(dependent_service:Service)
        OPTIONAL MATCH (person:Person)-[:HAS_SKILL]->(skill:Skill)

        WHERE skill.name IN split(service.tech_stack, ',')

        WITH person,
             count(DISTINCT dependent_service) as dependency_count,
             avg(toFloat(skill.level)) as avg_skill_level

        RETURN {
            person_name: person.name,
            email: person.email,
            expertise_match: avg_skill_level,
            dependent_services: dependency_count
        } as recommendation
        ORDER BY avg_skill_level DESC
        LIMIT 1
        """

        with self.driver.session() as session:
            result = session.run(query, service_id=service_id)
            record = result.single()
            return record['recommendation'] if record else None

    def create_org_snapshot(self, snapshot_date: str) -> bool:
        """
        Create a historical snapshot of org structure

        Args:
            snapshot_date: Date of snapshot (ISO format)

        Returns:
            True if successful
        """
        query = """
        MATCH (person:Person)
        OPTIONAL MATCH (person)-[:MEMBER_OF]->(team:Team)
        OPTIONAL MATCH (person)-[:HAS_SKILL]->(skill:Skill)

        CREATE (snapshot:OrgSnapshot {
            date: $snapshot_date,
            created_at: datetime(),
            person_count: count(DISTINCT person),
            team_count: count(DISTINCT team),
            skill_count: count(DISTINCT skill)
        })

        WITH snapshot, person, team, skill
        CREATE (snapshot)-[:SNAPSHOT_OF_PERSON]->(person)
        CREATE (snapshot)-[:SNAPSHOT_OF_TEAM]->(team)

        RETURN snapshot
        """

        with self.driver.session() as session:
            try:
                session.run(query, snapshot_date=snapshot_date)
                logger.info(f"Created org snapshot for {snapshot_date}")
                return True
            except Exception as e:
                logger.error(f"Failed to create snapshot: {e}")
                return False

    def export_as_json(self, query: str) -> List[Dict[str, Any]]:
        """
        Export query results as JSON

        Args:
            query: Cypher query

        Returns:
            List of dictionaries
        """
        with self.driver.session() as session:
            result = session.run(query)
            return [dict(record) for record in result]


# Example usage
if __name__ == "__main__":
    from neo4j import GraphDatabase

    # Initialize
    driver = GraphDatabase.driver(
        "bolt://localhost:7687",
        auth=("neo4j", "password")
    )

    builder = GraphQueryBuilder(driver)

    # Get org hierarchy for a person
    hierarchy = builder.get_organizational_hierarchy("p-001")
    print(f"Person: {hierarchy['person']['name']}")
    print(f"Team: {hierarchy['team']['name'] if hierarchy['team'] else 'None'}")
    print(f"Teammates: {[t['name'] for t in hierarchy['teammates']]}")

    # Find skill gaps
    gaps = builder.find_team_skill_gaps(
        "t-001",
        ["Java", "Python", "Kubernetes", "AWS"]
    )
    print(f"\nTeam skill coverage: {gaps['coverage']:.1f}%")
    print(f"Gaps: {gaps['gaps']}")

    # Find cross-team dependencies
    dependencies = builder.get_cross_team_dependencies()
    for dep in dependencies:
        print(f"\n{dep['fromTeam']} → {dep['toTeam']} "
              f"({dep['dependencyCount']} services)")

    # Find service owner recommendation
    owner = builder.recommend_service_owner("s-001")
    if owner:
        print(f"\nRecommended owner: {owner['person_name']}")

    driver.close()
