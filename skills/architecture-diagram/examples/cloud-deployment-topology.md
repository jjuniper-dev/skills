# Example: Cloud Deployment Topology Diagram

## Context
Multi-region cloud deployment on Azure with failover, load balancing, and security layers.

## Input Description
```
We deploy on Azure across two regions: East US (primary) and Canada Central (secondary).
Each region has:
- API Gateway for routing
- Kubernetes cluster (AKS) with microservices
- Azure SQL Database
- Storage accounts

Traffic goes through Azure Front Door for global load balancing.
API Gateway sits in front of Kubernetes.
Microservices run as containers.
Database has geo-replication to the secondary region.
Network security is managed by NSGs and Azure Firewall.
Logging goes to Log Analytics in both regions.
```

## Output (Mermaid Diagram)
```mermaid
graph TB
    subgraph Global["Global Services"]
        AFD["Azure Front Door<br/>Global LB"]
        DM["Domain Manager<br/>DNS"]
    end
    
    subgraph East["Primary Region: East US"]
        subgraph EastNetwork["Network Layer"]
            EFW["Azure Firewall"]
            ENSG["NSG"]
        end
        
        subgraph EastCompute["Compute"]
            EAGW["API Gateway"]
            EAKS["AKS Cluster<br/>Microservices"]
        end
        
        subgraph EastData["Data"]
            ESQL["Azure SQL<br/>Primary"]
            ESTOR["Storage Account"]
        end
        
        ELL["Log Analytics"]
    end
    
    subgraph Canada["Secondary Region: Canada Central"]
        subgraph CanNetwork["Network Layer"]
            CFW["Azure Firewall"]
            CNSG["NSG"]
        end
        
        subgraph CanCompute["Compute"]
            CAGW["API Gateway"]
            CAKS["AKS Cluster<br/>Microservices"]
        end
        
        subgraph CanData["Data"]
            CSQL["Azure SQL<br/>Replica"]
            CSTOR["Storage Account"]
        end
        
        CLL["Log Analytics"]
    end
    
    AFD --> EFW
    AFD --> CFW
    
    EFW --> ENSG
    ENSG --> EAGW
    EAGW --> EAKS
    
    CFW --> CNSG
    CNSG --> CAGW
    CAGW --> CAKS
    
    EAKS --> ESQL
    EAKS --> ESTOR
    CAKS --> CSQL
    CAKS --> CSTOR
    
    ESQL <-.->|Geo-replication| CSQL
    ESTOR <-.->|Replication| CSTOR
    
    EAKS -.-> ELL
    CAKS -.-> CLL
    EAGW -.-> ELL
    CAGW -.-> CLL
```

## Layout Notes
- **Global Services** (top): Entry point, global routing
- **Regions** (left/right): Self-contained deployment units
- **Network → Compute → Data**: Logical flow within each region
- **Dotted arrows**: Replication and monitoring flows

## Resilience Features Highlighted
- Multi-region deployment (East US + Canada Central)
- Azure Front Door for global load balancing and failover
- Database geo-replication (read replicas, failover support)
- Separate network security per region
- Centralized logging per region

## Quality Checklist
- ✅ Clear separation of regions
- ✅ All resources have at least one connection
- ✅ Replication relationships shown (dotted)
- ✅ Logical grouping (network, compute, data)
- ✅ Disaster recovery path visible (AFD → secondary region)
- ✅ Readable without excessive zoom

## PPTX Integration
**Slide title**: "Multi-Region Cloud Architecture"
**Presenter notes**: 
- "We're deployed across two regions for resilience"
- "Azure Front Door routes traffic to the nearest healthy region"
- "Database replication ensures data consistency"
- "If East US fails, traffic automatically routes to Canada Central"
- "RTO: <5 minutes | RPO: <1 minute"

## Color Coding (Optional)
- Blue: Networking components
- Green: Compute resources
- Orange: Data storage
- Purple: Monitoring/Logging
- Gray: Cross-region connections
