# AWS Lambda

## Testing AWS Lambda Locally with SAM

### Setting up CloudFormation

1. Create the cloud formation `template.yaml` file
2. Add the Lambda Function, identifying the uri, handler and valid runtime string (check AWS documentation for list of supported runtimes)
3. To emulate Lambda functions being used through API Gateway, add an events property setting the GET resource, api pathway and HTTP verb

### Setting up Lambda

1. Create the lambda function, with the event handler function as defined in the Cloud Formation template
2. return a valid HTTP response, capturing information from the event if desired
3. Create a sample event JSON. This will be sent to the event handler
4. Run `sam local invoke -e {pathToEvent} {nameOfFunction}`. For example, `sam local invoke -e lambda/lambda_event.json LambdaExampleFunction`
5. A docker instance should spin up and logs should notify of the result

### Setting up API Gateway

1. To incorporate API gateway, follow similar instructions and create a function with an event handler
2. return a valid HTTP response, capturing information from the HTTP request that might be useful in the application (i.e. `queryStringParameters` or `body`)
3. Create a sample event JSON, using a typical HTTP request. This will be sent to the event handler via API Gateway
4. Run `sam local invoke -e {pathToEvent} {nameOfFunction}`. For example `sam local invoke -e api_gateway/api_gateway_event.json APIGatewayExampleFunction`
5. A docker instance should spin up and logs should display the result

### Setting up a SAM Local Server

1. To create a live server run `sam local start-api` which will spin up a server on port 3000. Using the pathway endpoint defined in the CloudFormation template, you can test the API by using web browser or Postman
