# Skill: Neo4j Graph Builder

## Purpose
Generate Neo4j graph database schemas, Cypher queries, and graph models from natural language descriptions of relationships, entities, and data structures.

## When to use
- Building knowledge graphs
- Mapping organizational structures, dependencies, or relationships
- Creating network analysis models
- Establishing entity relationship models for graph databases
- Integrating data source mappings
- Governance and compliance tracking networks

## Inputs
- Entity descriptions (types, properties, relationships)
- Relationship definitions (how entities connect)
- Natural language description of data model
- Optional: existing Neo4j schema or DDL
- Optional: sample data or use cases

## Outputs
- Neo4j Cypher DDL (CREATE INDEX, CREATE CONSTRAINT)
- Sample Cypher queries (MATCH, CREATE, MERGE patterns)
- Graph schema documentation
- Data ingestion patterns
- Query performance notes

## Constraints
- Relationships must be explicitly typed
- Property names follow naming conventions (camelCase or snake_case)
- No orphan nodes without relationships
- Avoid redundant properties (normalize appropriately)
- Indexes defined on high-query properties
- Unique constraints where applicable

## Workflow
1. **Parse entities** - Identify node types and their properties
2. **Map relationships** - Define relationship types and directionality
3. **Normalize schema** - Remove redundancy, define indexes/constraints
4. **Generate Cypher** - CREATE statements, sample MATCH queries
5. **Create patterns** - Common traversal and aggregation patterns
6. **Document graph** - Schema diagram, property guide, query examples
7. **Validate completeness** - No orphan nodes, all relationships typed

## Quality checks
- Schema is normalized (properties not duplicated across relationships)
- All relationships are bidirectional where appropriate
- Indexes cover common query patterns
- Cypher queries are idiomatic
- Schema documentation includes use cases
- Performance considerations documented
- Sample data aligns with schema

## Output formats
- Cypher DDL statements
- JSON schema representation
- Mermaid/PlantUML graph diagram
- Query recipe book
- Migration/ingestion guide

## Examples
- Organizational hierarchy (teams, roles, reporting)
- Application/service dependency graph
- Data lineage network
- Regulatory compliance mapping
- Skill/capability matrix
- Technology stack and integration graph
