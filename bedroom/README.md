# Cloudformation turn on the lights.

This repo contains cloudformation templates for a simple POC wher I create an elasticbeanstalk sample, but before cloudformation triggers the lambda function that simulates the lights of a bedroom lighting up. I do not use any IOT device, the bedroom is just a S3 bucket hosting a static site. The POC aims to test how cloudformation can be extensible to the AWS services and how to integrates with third party services.

## Steps

### Create bucket.
```
aws cloudformation create-stack --stack-name bedroom-s3 --template-body file://s3.yaml
```

### Upload code.

Update the bucket-name of the script.
```
./deploy.sh
```

### Create Lambda.
```
aws cloudformation create-stack --stack-name bedroom-lambda --template-body file://lambda.yaml --capabilities CAPABILITY_IAM
```

### Create elasticbeanstalk.

Update the elasticbeanstalk.yaml with the lambda ARN before run the command for the elasticbeanstalk environment createion.
```
aws cloudformation create-stack --stack-name elasticbeanstalk --template-body file://elasticbeanstalk.yaml
```
