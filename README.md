# Globant Data Engineering Challenge
## Prerequisites
- Python 3.9
- Docker
- AWS Account
## Solution Architecture
To solve this challenge, Python and Flask were using to develop a Rest API. As database MySQL was chose, and to perform database operations SQLAlchemy. API and Database were deployed on AWS Lightsail.
<p align="center">
  <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/19482586/285673257-f5d3a531-60c6-4bfb-b036-5c05294d80da.png" width="60%">
</p>

## Database model
It has 3 tables: hired_employees, departments and jobs. Table hired_employees has 2 FK to the other ones, and record_inserted_datetime and upload_filename were added to all tables as a way to keep track of changes.
<p align="center">
  <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/19482586/285673459-32dfa204-fb98-4cf0-841d-3f078c3604ac.png" width="60%" align="center">
</p>

## API Rest
A Docker image was generated and then pushed to AWS LightSail.
It has 5 methods:
https://glb-api-rest-service.iavds3kkig434.us-east-1.cs.amazonlightsail.com/
### POST
- /jobs/load-data
- /departments/load-data
- /hired-employees/load-data
### GET
- /reports/hires-per-quarter
- /reports/departments-mean-hires

![image](https://github.com/jeanpaulrd1/glb-data-engineering-challenge/assets/19482586/f717b35a-1566-44eb-980a-6e9cc9407a44)


## Database
A MySQL instance was deployed on AWS LightSail.

![image](https://github.com/jeanpaulrd1/glb-data-engineering-challenge/assets/19482586/64cda0c8-f6cc-4f00-b4a0-f89423329bbc)
