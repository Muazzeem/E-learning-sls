import boto3
import json
import requests


def token_validation(token):
    url = "https://www.google.com/recaptcha/api/siteverify"
    params = {
        "secret": "6LcTZwEeAAAAAFYVeQbFJQGSc8YZOWjlyLNZ8cDB",
        "response": token,
    }
    verify_rs = requests.post(url, data=params)
    recaptcha_rs = json.loads(verify_rs.text)
    return recaptcha_rs["success"]


def lambda_handler(event, context):
    data = json.loads(event["body"])
    email = data["email"]
    name = data["name"]
    phone = data.get("phone", "")
    message = data["message"]
    response = {
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*"
        },
        'body': {'error': 'Invalid reCapcha token.'},
        'statusCode': 200,
    }
    local_token = "a25db276-58a9-11ec-bf63-0242ac130002"
    if token_validation(data["token"]) is True or data["token"] == local_token:
        pass
    response["body"] = json.dumps(data)
    return response
