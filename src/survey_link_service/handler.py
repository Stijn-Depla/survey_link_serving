"""
Handler wrapping pipeline in a Lambda friendly function
"""
import json

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
    i_method = event["httpMethod"]
    if i_method == "GET":
        dict_event_action = json.loads(event['body'])['action']
        t_result = pipeline_serve_link(dict_event_action)
        print("Status_code returned by pipeline_serve_link: " + str(t_result[0]))
        print("Message returned by pipeline_serve_link: " + t_result[1])
        print("Link returned by pipeline_serve_link: " + str(t_result[2]))
        if t_result[2] is not None:
            return {
                "statusCode": t_result[0],
                "headers": {"link": str(t_result[2])},
                "isBase64Encoded": False,
            }
        return {
            "statusCode": t_result[0],
            "headers": {},
            "body": t_result[1],
            "isBase64Encoded": False,
        }
    return {
        "statusCode": 400,
        "headers": {},
        "body": "API hanldes GET requests only",
        "isBase64Encoded": False,
    }
