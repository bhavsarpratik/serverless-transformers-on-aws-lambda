# End2End Serverless Transformers On AWS Lambda for NLP 🚀

<figure>
<img src="https://github.com/bhavsarpratik/serverless-transformers-on-aws-lambda/blob/master/.github/banner.jpg?raw=true" width="75%" height="75%" alt="">
<figcaption>You need no servers</figcaption>
</figure>

## Deploy transformers with ease 💆‍♂️

Go through this [video](https://www.youtube.com/watch?v=EoazSUJyGbs) and [slide deck](https://bit.ly/serverless-transformers) for full info.

Current available pipelines
1. classification
2. sentence encoding 
3. translation **(coming soon)**
4. token classification 
5. text generation
6. zero shot classification

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
- update ECR path in the workflow
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
