# Case Study Solution

## Design Diagram

[IMAGE]

## Explanation
Currently, the application is a *monolithic* e-commerce web/mobile app. The following challenges were identified:

* Difficulties scaling to meet demand spikes. Likely, due to the monolithic set up, scaling is mostly vertical and not automated. 
* Changes take long to be deployed to production: lack of agility. 
* Changes often introduce bugs that involve multiple teams to remediate: lack of deployment autonomy, siloed teams, tight coupling.
* Newly introduced changes can break existing external integrations: poorly implemented API versioning and/or lack of standardization.

This is a long-term transformation, therefore major technical and organizational changes are proposed.

A microservices design is proposed to tackle these challenges effectively. The following services are suggested based on business capabilities and shared functions:

* Stateless Services
    * Web UI service: serves the frontend for Web users
    * Mobile UI service: serves the frontend for Mobile users
    * Authentication service: centralizes user authentication functions
    * Reporting service: centralizes reporting functions
    * Payment service: connector service that mediates requests to external payment services
* Stateful Services
    * Customer service: service that maintains customer information (user profiles)
    * Cart service: service responsible for online carts
    * Orders service: service that processes orders and maintains information about orders
    * Analytics service: service responsible for analytics that maintains a data warehouse
    * Inventory service: service that maintains inventory information
    * Shipping service: service that processes shipping and maintains shipping information 
    * Order History service: serves order history data with read-only views aggregated from orders and shipping services

The following guidelines and principles are proposed in conjunction with this design:

* Independent deployability: ensure each service own its entire domain logic and does not depend on another service to operate its internal functions. Services should be able to be deployed independently and by different teams without affecting others.
* Data isolation: ensure each database is owned by a single service and no other service can write directly to it. Any read/write operation must be requested via the owning service's interface. Application and data are decoupled: databases are "attached" resources, but applications run as stateless processes that communicates with its (external) database.
* Standardized APIs: each service must have a clearly defined API through which all interactions happen. A contract must be established by using specification standards such as Open API 2.0. 
* API Gateway pattern: Ensure an API Gateway is present to provide a single point of entry for users. Operations that span multiple services can be aggregated at the API Gateway to reduce network round trips. Web- and Mobile-specific APIs can be differentiated at the gateway. 
* CI/CD pipelines: all deployments (including infrastructure and applications) must be automated via CI/CD pipelines. Dev/Test and Production environments must be as similar as possible.  
* Site Reliability Engineering (SRE): current ways of working must shift and align with an SRE model and culture. 

## Suggested Implementation (High Level)
Start with SRE training for your teams and aim to reach a basic level of SRE maturity.

Restructure and train teams so that they are cross-functional and able to implement the full stack of technologies for their respective domains.

The recommended hosting platform for all workloads is Google Kubernetes Engine (GKE). The choice of database technology depends on the requirements of each data and is summarized in the following table:

| Service       | Database          | Comments   |
| ------------- |:-----------------:| :----------|
| Customer      | Cloud Firestore   | Non-relational, scalable database for user profiles
| Cart          | Memorystore       | Fast-access memory database are ideal for cart sessions
| Orders        | Cloud SQL         | Orders require a transactional database 
| Analytics     | Cloud BigQuery    | Ideal as Data Warehouse
| Inventory     | Cloud SQL         | Inventory data may require transactions / relational model
| Shipping      | Cloud SQL         | Shipping data may require transactions / relational model
| Order History | Cloud SQL         | Will be a read replica with data from Orders and Shipping service. Using Cloud SQL will work best.

The workloads can be implemented on a single GKE cluster, using different namespaces for frontend, backend, and utility (auth & reporting) services.

Each microservices must implement an HTTP REST API. Contractualize APIs using Open API 2.0.

GCP's API Gateway service can be used to implement the API Gateway pattern.

Cloud Deployment Manager or Terraform can be used for infrastructure deployment and automation. Cloud Build or similar third-party service can be used for CI/CD.

Cloud Pub/Sub can be leveraged for asynchronous messaging between microservices.
