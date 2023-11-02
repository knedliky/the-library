import json


def lambda_handler(event, context):
    
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }

# sam local invoke -e lambda/lambda_event.json LambdaExampleFunction