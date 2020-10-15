"""
Handler wrapping pipeline in a Lambda friendly function
"""
from dotenv import load_dotenv
from os import environ

try:
    from pipeline import pipeline_serve_link
except ModuleNotFoundError:
    from .pipeline import pipeline_serve_link


def call(event, context):
    """
    Lambda function to wrap around pipeline that generates new survey link when called

    Returns
    -------
    response: dict
        Contents for API response to notify Trello

    """
    print(event)
    try:
        load_dotenv('./.env')
        i_trusted_origin = environ['TRUSTED_ORIGIN']
        i_method = event["httpMethod"]
        i_origin = event['headers']['origin']
        if i_method == "GET" and i_origin == i_trusted_origin:
            t_result = pipeline_serve_link()
            print("Status_code returned by pipeline_serve_link: " + str(t_result[0]))
            print("Message returned by pipeline_serve_link: " + t_result[1])
            print("Link returned by pipeline_serve_link: " + t_result[2])
            if isinstance(t_result[2], str):
                return {
                    "statusCode": t_result[0],
                    "headers": {
                        "Message": t_result[1],
                        "Access-Control-Allow-Methods": "Get",
                        "Access-Control-Allow-Origin": i_trusted_origin
                    },
                    "body": t_result[2],
                    "isBase64Encoded": False,
                }
            return {
                "statusCode": t_result[0],
                "headers": {
                    "Message": t_result[1],
                    "Access-Control-Allow-Methods": "Get",
                    "Access-Control-Allow-Origin": i_trusted_origin
                },
                "body": "Pipeline produced no link",
                "isBase64Encoded": False,
            }
        return {
            "statusCode": 400,
            "headers": {},
            "body": "This service is not meant for you with method: " + i_method + "and origin: " + i_origin,
            "isBase64Encoded": False,
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "headers": {},
            "body": "Service had an internal error: " + str(e),
            "isBase64Encoded": False,
        }
