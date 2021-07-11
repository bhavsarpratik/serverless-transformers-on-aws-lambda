# End2End Serverless Transformers On AWS Lambda for NLP 🚀

Deploy transformers serverless on AWS Lambda with ease 💆‍♂️

Current available pipelines
1. classification
1. translation (coming soon)
1. token classification (need contribution)
1. text generation (need contribution)
1. zero shot classification (need contribution)

## What you get with this?
- ability to run transformers without servers
- complete CI/CD
- concurrency upto 1000 (default AWS limit)
## How to use this?
- clone the repo
- keep the pipeline folder you want to use
- modify the source and tests
- keep the corresponding github action in `.github/workflows`
- modify directory, registry and lambda function name in workflow
- create repository in AWS ECR
- set up secrets in repo (needed for access to AWS; this creds should have access to ECR and Lambda)
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
- push the code
- create PR
    - this will build the container
    - run all the tests
    - push container to ECR registry
    - update lambda with the new container (this will not happen when you push the first time)
- create lambda function if it does not exist
    - give appropriate IAM role
    - set timeout and RAM
- create API in API gateway and link to lambda

Done! Now you can call the lambda using the API