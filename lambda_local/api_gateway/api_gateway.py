import json


def gateway_handler(event, context):
    # if event['body'] is None:
    #      return {"statusCode": 200, "body": "No body"}
    return {"statusCode": 200, "body": json.dumps(event['queryStringParameters'])}

# sam local invoke -e api_gateway/api_gateway_event.json APIGatewayExampleFunction
# sam local start-api