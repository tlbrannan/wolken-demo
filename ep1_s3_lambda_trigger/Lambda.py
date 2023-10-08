import json


def lambda_handler(event, context):
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    file_name = event["Records"][0]["s3"]["object"]["key"]

    print(f"Bucket Name: {bucket_name}")
    print(f"File Name: {file_name}")
