EKS Cluster creation steps
    1. Create EKS cluster master node.
    2. Create Node groups in the EKS cluster
    3. Create OIDC connection in the AWS Identity provider with EKS cluster
    4. Install Kubernetes dashboard for monitoring
    5. Install AWS Load balancer controller

Create ECR repository for the docker image

EKS Yamls for our application
    1. Create deployment yaml
    2. create service yaml
    3. create ingress yaml


Code Pipeline for EKS
    1. Create 2 code commit repostories
        one for flask ml application and another one for EKS yamls
    2. Create 2 code build projects
        one for flask ml application and another one for EKS yamls
    3. Create 2 code pipeline 
        one for flask ml application and another one for EKS yamls
        In the EKS yaml code pipeline, have both ECR repo and code commit repo as the source


Push ML application into EKS
    1. Create Flask application for our ML Application
    2. Convert that Flask application into a docker Application
    3. Test the docker application in your local
    4. Push the Flask code to code commit, check the pipeline runs with out any issues. 
    5. Once the Flask code pipeline ran successfully, check wether it triggers the second EKS yaml code pipeline. 
    6. If the second pipeline is triggered, check the API response for the update values.
