# Template: Control Plane Architecture

## Purpose
Standardized layout for control plane architectures (e.g., PATH-style governance layer).

## Layout
Top → Governance / Control Plane
Middle → Runtime / Workloads
Bottom → Data Layer

## Elements
- Identity (Entra ID)
- API Gateway (APIM)
- Policy (Azure Policy)
- Monitoring (Log Analytics / App Insights)
- Data Governance (Purview)

## Rules
- Control plane spans all layers
- Flows are directional
- Audit/logging always present
- No orphan services

## Output pattern
Layered diagram with clear separation of governance vs runtime
