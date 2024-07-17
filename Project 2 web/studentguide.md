# Project 2 Overview
As an aspiring Solutions Architect, you will build a multi-tier architecture utilizing AWS Cloud Infrastructure. [example shown below]

![architecture](https://github.com/skillstorm-congo/AWS-DevOps-StarterKit/blob/364c551c6b1defdd5f4ae7962072faf5e4ea997a/Projects/Project%202/architecture.png)

## Core Requirements: 
**5-minute presentation and working environment**
-	Prepare a presentation that covers a visual diagram of your architecture (ex: Lucid Chart), the purpose of what you have built, and any lessons learned
-	Demonstrate a working project that builds a multi-tier architecture and solution:
-	*example* deploy a virtual network across multiple availability zones in a region using CloudFormation, and implement resources such as DynamoDB, EFS, Lambda.
-	Data tier: RDS; Storage tier: EFS, NFS; Presentation tier: EC2
-	Your infrastructure must support both public and private access for the company’s requirements

## Project Outline
-	Everett Enterprises is a marketing agency for major media companies. They currently host their business in an on-premises data center but have decided to move to the cloud due to the financial and performance improvements. They have a website that is utilized by their clients, and it is urgent that they have a working environment for their business requirements. 
-	You have been hired to assist their company with the transition. You must design a fast, scalable, reliable, and cost-effective solution to replace their on-premises infrastructure. 
-	For this project, you will build a multi-tier architecture in AWS. *example* a serverless presentation tier: S3 and data tier: DynamoDB. You may use your creativity (and are highly encouraged) to expand upon this. Key requirements are listed above, basic outline is listed below in instructions.

## Project Instructions
-	You will be working in a team, separate responsibilities to accomplish project goals
-	There will be a survey at the end to determine participation
-	The instructions below are an example of what you could build out in Project 2, you may use these or build your own architecture.

### Example Project
-	Your Trainer will provide the files from [our repo](https://github.com/skillstorm-congo/AWS-DevOps-StarterKit/tree/main/Projects/Project%202/Resources/movies-in-progress-main)
-	Install [node.js - LTS](https://nodejs.org/en/blog/release/v16.16.0/)
   - VERSION 16.6
-	Use npm commands to deploy your build
-	There will be many files cloned, you will be updating: 
    -	create-movie.py
    -	read-movies.js
    -	.env
-	Create a DynamoDB table
    -	Partition key: title
    -	Sort key: director
-	IAM (Identity and Access Management): Create role for Lambda to access DynamoDB
-	Create (2) Lambda functions that push the data to DynamoDB
    -	(a) one to read
    -	(b) one to write
-	API Gateway: 
    -	Build REST API (private)
    -	Create resource for movies
    -	Create (2) methods:
    -	GET
    -	POST
    -	You will need the Invoke URL (aka: Gateway_URI) for your .env file
    -	Hint: do not add a forward or backslash to the beginning or end of the address
-	NPM commands you may need:
    -	npm install
    -	npm start
    -	npm run build
        -	This will create a build folder in VS Code, you will need this for S3
-	S3: Create a single bucket for your team
    -	Configure static website hosting
    -	Modify bucket policy
    -	Copy the contents of the build folder to the S3 bucket you created
    -	Copy the static website URL
-	Bonus: integrate CloudFront
-	**Final objective for project:**
    -	Deploy code in Lambda
    -	Include more movie items by:
    -	A) Adding data to form that is on your S3 website OR
    -	b) Advanced Option: Modifying Python or JavaScript: [guide](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html)
    -	See your modifications using the S3 static website URL

-----------------------------------------------------------------------------------------------------------------------------------------
## Project Video Guides
These videos are screen grabs of a working environment of the Project 2 minimum requirements. 

Use these as a *baseline* for your working environment. **Do not save, record, or re-distribute any of the below items**

### Project 2 - Example 1
[Advanced Option Demo - Excluding API Gateway](https://skillstorm-my.sharepoint.com/:v:/p/vbraun/Efa38cZmwcFEo8t8jktEG38BcvT44CwgsqSbu8er2ss7Tg)

### Project 2 - Example 2
Lab 7 - Fully Built Configuration (not a demo)

[Cloudformation Stack](https://skillstorm-my.sharepoint.com/:v:/p/vbraun/EW3KyTLl6AFBui6lI3HYei0B8Aw2TNXcOYvruBTpWgYJwQ?e=UtCGC6)

[ASG](https://skillstorm-my.sharepoint.com/:v:/p/vbraun/EW0jiJ6LS59LrNCN_92ciIABT3BiFKnvQrUxUtGIvV1H2g?e=ddhytR)

[ASG Running](https://skillstorm-my.sharepoint.com/:v:/p/vbraun/EXK-FTI0C_NIss4LBXCfgYoBscAKiElL_2mxNIS-1PGaOw?e=ZyN0Yx)

[All Configuration Details](https://skillstorm-my.sharepoint.com/:v:/p/vbraun/EcdN3VjssndCpOM8zkupcWoBf68rhusC3K_SM1iec90_fQ?e=yV4izz)

[Project 2 Final Result Example](https://skillstorm-my.sharepoint.com/:v:/p/vbraun/EaYs8IcGwGNImfGhFr43bsYBVNtufvBjlQkLvjdqGlnXmQ?e=PUChKT)


### Project 2 - Example 3
[MySQL Wordpress Demo](https://skillstorm-my.sharepoint.com/:v:/p/vbraun/ETH7Iquc6lNGjV6bYRgezQIBjhMswRSYBpxyXzMFMuMNUw)

-----------------------------------------------------------------------------------------------------------------------------------------
## Hints
•	Utilize documentation to find helpful hints (ex: API Gateway, Python, Lambda...)
•	Do not wait until the week of to complete your project
•	Use Lab 7 (Capstone) as a baseline/idea


