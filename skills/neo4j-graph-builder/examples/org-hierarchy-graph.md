# Example: Organizational Hierarchy Graph

## Use Case
Model organizational structure, reporting relationships, team assignments, and role information.

## Input Description
```
Build a graph for a tech company structure:
- CEO reports to Board
- Two SVPs: Engineering and Product
- Engineering has 3 teams: Platform, Backend, DevOps
- Product has 2 teams: Design, Product Management
- Each team has team members with roles
- Team members have skills and certifications
- Teams own microservices
- Services have dependencies
```

## Cypher DDL (Schema)

```cypher
-- Create constraints
CREATE CONSTRAINT person_id ON (p:Person) ASSERT p.id IS UNIQUE;
CREATE CONSTRAINT team_id ON (t:Team) ASSERT t.id IS UNIQUE;
CREATE CONSTRAINT service_id ON (s:Service) ASSERT s.id IS UNIQUE;
CREATE CONSTRAINT skill_id ON (sk:Skill) ASSERT sk.id IS UNIQUE;

-- Create indexes
CREATE INDEX idx_person_email ON (p:Person) FOR (p.email);
CREATE INDEX idx_team_name ON (t:Team) FOR (t.name);
CREATE INDEX idx_service_name ON (s:Service) FOR (s.name);
```

## Sample Data (CREATE statements)

```cypher
-- Create organization structure
CREATE (board:Organization {id: "org-001", name: "Board", level: "governance"})
CREATE (ceo:Person {id: "p-001", name: "Alice Chen", email: "alice@company.com", level: "C-suite", role: "CEO"})
CREATE (svp_eng:Person {id: "p-002", name: "Bob Kumar", email: "bob@company.com", level: "SVP", role: "SVP Engineering"})
CREATE (svp_prod:Person {id: "p-003", name: "Carol Martinez", email: "carol@company.com", level: "SVP", role: "SVP Product"})

-- Create teams
CREATE (team_platform:Team {id: "t-001", name: "Platform Team", description: "Core infrastructure and shared services", createdDate: "2024-01-15"})
CREATE (team_backend:Team {id: "t-002", name: "Backend Team", description: "API and business logic services", createdDate: "2024-01-15"})
CREATE (team_devops:Team {id: "t-003", name: "DevOps Team", description: "Infrastructure and deployment", createdDate: "2024-02-01"})
CREATE (team_design:Team {id: "t-004", name: "Design Team", description: "UX and product design", createdDate: "2024-01-15"})
CREATE (team_pm:Team {id: "t-005", name: "Product Management", description: "Product strategy and roadmap", createdDate: "2024-01-15"})

-- Create team members
CREATE (eng_lead:Person {id: "p-004", name: "Diana Chen", email: "diana@company.com", role: "Platform Tech Lead"})
CREATE (backend_eng1:Person {id: "p-005", name: "Evan Park", email: "evan@company.com", role: "Backend Engineer"})
CREATE (backend_eng2:Person {id: "p-006", name: "Fiona Lopez", email: "fiona@company.com", role: "Backend Engineer"})
CREATE (devops_eng:Person {id: "p-007", name: "George Kim", email: "george@company.com", role: "DevOps Engineer"})
CREATE (designer:Person {id: "p-008", name: "Helen Wright", email: "helen@company.com", role: "Senior Designer"})
CREATE (pm:Person {id: "p-009", name: "Ivan Petrov", email: "ivan@company.com", role: "Product Manager"})

-- Create skills
CREATE (skill_java:Skill {id: "sk-001", name: "Java", level: "advanced"})
CREATE (skill_python:Skill {id: "sk-002", name: "Python", level: "advanced"})
CREATE (skill_k8s:Skill {id: "sk-003", name: "Kubernetes", level: "expert"})
CREATE (skill_gcp:Skill {id: "sk-004", name: "GCP", level: "advanced"})
CREATE (skill_figma:Skill {id: "sk-005", name: "Figma", level: "expert"})
CREATE (skill_strategy:Skill {id: "sk-006", name: "Strategy", level: "advanced"})

-- Create services
CREATE (svc_auth:Service {id: "s-001", name: "Auth Service", tech_stack: "Java", owner_id: "t-001"})
CREATE (svc_api:Service {id: "s-002", name: "API Gateway", tech_stack: "Go", owner_id: "t-002"})
CREATE (svc_data:Service {id: "s-003", name: "Data Pipeline", tech_stack: "Python", owner_id: "t-001"})
CREATE (svc_ci:Service {id: "s-004", name: "CI/CD Pipeline", tech_stack: "Terraform", owner_id: "t-003"})

-- Create relationships: Reporting structure
CREATE (ceo)-[:REPORTS_TO]->(board)
CREATE (svp_eng)-[:REPORTS_TO]->(ceo)
CREATE (svp_prod)-[:REPORTS_TO]->(ceo)

-- Create relationships: Team leadership
CREATE (svp_eng)-[:LEADS]->(team_platform)
CREATE (svp_eng)-[:LEADS]->(team_backend)
CREATE (svp_eng)-[:LEADS]->(team_devops)
CREATE (svp_prod)-[:LEADS]->(team_design)
CREATE (svp_prod)-[:LEADS]->(team_pm)

-- Create relationships: Team members
CREATE (eng_lead)-[:MEMBER_OF]->(team_platform)
CREATE (backend_eng1)-[:MEMBER_OF]->(team_backend)
CREATE (backend_eng2)-[:MEMBER_OF]->(team_backend)
CREATE (devops_eng)-[:MEMBER_OF]->(team_devops)
CREATE (designer)-[:MEMBER_OF]->(team_design)
CREATE (pm)-[:MEMBER_OF]->(team_pm)

-- Create relationships: Skills
CREATE (eng_lead)-[:HAS_SKILL {proficiency: "expert", yearsExperience: 8}]->(skill_java)
CREATE (eng_lead)-[:HAS_SKILL {proficiency: "advanced", yearsExperience: 6}]->(skill_k8s)
CREATE (backend_eng1)-[:HAS_SKILL {proficiency: "advanced", yearsExperience: 5}]->(skill_java)
CREATE (backend_eng2)-[:HAS_SKILL {proficiency: "advanced", yearsExperience: 4}]->(skill_python)
CREATE (devops_eng)-[:HAS_SKILL {proficiency: "expert", yearsExperience: 7}]->(skill_k8s)
CREATE (devops_eng)-[:HAS_SKILL {proficiency: "advanced", yearsExperience: 6}]->(skill_gcp)
CREATE (designer)-[:HAS_SKILL {proficiency: "expert", yearsExperience: 9}]->(skill_figma)
CREATE (pm)-[:HAS_SKILL {proficiency: "advanced", yearsExperience: 10}]->(skill_strategy)

-- Create relationships: Service ownership
CREATE (team_platform)-[:OWNS]->(svc_auth)
CREATE (team_platform)-[:OWNS]->(svc_data)
CREATE (team_backend)-[:OWNS]->(svc_api)
CREATE (team_devops)-[:OWNS]->(svc_ci)

-- Create relationships: Service dependencies
CREATE (svc_api)-[:DEPENDS_ON]->(svc_auth)
CREATE (svc_data)-[:DEPENDS_ON]->(svc_auth)
CREATE (svc_ci)-[:DEPENDS_ON]->(svc_api)
```

## Common Queries

```cypher
-- Find all people reporting to SVP Engineering (direct + transitive)
MATCH (svp:Person {id: "p-002"})<-[:REPORTS_TO*]-(person:Person)
RETURN person.name, person.role
ORDER BY person.name;

-- Find teams and their members
MATCH (team:Team)<-[:MEMBER_OF]-(person:Person)
RETURN team.name, collect(person.name) as members
ORDER BY team.name;

-- Find people with a specific skill
MATCH (person:Person)-[:HAS_SKILL {proficiency: "expert"}]->(skill:Skill)
WHERE skill.name = "Kubernetes"
RETURN person.name, person.email, person.role;

-- Find service dependencies (transitive)
MATCH path=(svc:Service)-[:DEPENDS_ON*]->(dep:Service)
RETURN svc.name as service, dep.name as dependency;

-- Find team gaps: services without owners
MATCH (svc:Service)
WHERE NOT (svc)<-[:OWNS]-(:Team)
RETURN svc.name, svc.tech_stack;

-- Find cross-team dependencies
MATCH (t1:Team)-[:OWNS]->(s1:Service)-[:DEPENDS_ON]->(s2:Service)<-[:OWNS]-(t2:Team)
WHERE t1.id <> t2.id
RETURN t1.name as from_team, t2.name as to_team, collect(s1.name + "->" + s2.name) as dependencies;

-- Organizational structure (org chart)
MATCH (person:Person)-[:REPORTS_TO*0..3]-(top:Person)
WHERE NOT (top)-[:REPORTS_TO]->()
RETURN person.name, person.role, top.name as reports_to;
```

## Schema Diagram (Text)
```
Person --REPORTS_TO--> Person (hierarchy)
Person --MEMBER_OF--> Team (team assignment)
Person --HAS_SKILL--> Skill (capability tracking)
Team --LEADS--> Team (team hierarchy)
Team --OWNS--> Service (ownership)
Service --DEPENDS_ON--> Service (dependencies)
Organization --CONTAINS--> Team (org structure)
```

## Data Quality Checklist
- ✅ All people have unique IDs and emails
- ✅ All teams have names and descriptions
- ✅ Reporting relationships form a tree (no cycles)
- ✅ Service dependencies don't have cycles
- ✅ All services have an owner (team)
- ✅ All team members belong to a team
- ✅ Skill proficiency levels are consistent (novice, intermediate, advanced, expert)

## Maintenance Notes
- **Update frequency**: Weekly (org changes, skills)
- **Archive**: Keep historical snapshots for trend analysis
- **Validation**: Run cycle detection quarterly on reporting and dependencies
