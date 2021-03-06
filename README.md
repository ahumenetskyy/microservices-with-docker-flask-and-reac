# Microservices with Docker, Flask, and React [![Build Status](https://travis-ci.org/ahumenetskyy/microservices-with-docker-flask-and-reac.svg?branch=master)](https://travis-ci.org/ahumenetskyy/microservices-with-docker-flask-and-reac)

## General
Microservice web app based on [tutorial](https://testdriven.io/courses/microservices-with-docker-flask-and-react/).

Why? To get/improve practical skills.

### Services
1. users - server-side Flask app for managing users and auth
2. client - client-side React app
3. nginx - reverse proxy web server
4. swagger - Swagger API docs
5. scores - server-side Flask app for managing user scores
6. exercises - server-side Flask app for managing exercises

### App
![microservice architecture](https://testdriven.io/static/images/courses/microservices/07_testdriven.png "microservice architecture")
### Tools and Technologies
1. Python
2. Flask
3. Docker
4. Postgres
5. Node and NPM
6. React
7. Cypress
8. Swagger
9. Amazon Web Services (AWS)

### Concepts
1. Microservice Architecture
2. Test-Driven Development (TDD)
3. Continuous Integration (CI)
4. Continuous Delivery (CD)
5. Code Coverage
6. Code Quality
7. Token-based Authentication
8. Containerization
9. Container Orchestration
10. Serverless Architecture

## HOW-TOs

### How to deploy
1. Switch to prod virtual machine
    1. docker-machine env testdriven-prod3
    2. $ eval $(docker-machine env testdriven-prod3)
2. Re-build and up cotainers
    1. docker-compose -f docker-compose-prod.yml up -d --build

### Back to development env
1. eval $(docker-machine env -u)
