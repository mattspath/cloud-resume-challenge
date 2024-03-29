# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import boto3
import os

# Create dynamodb boto3 resource
dynamodb = boto3.resource('dynamodb')
# Set dynamodb table name variable from env
#ddbTableName = os.environ['databaseName']
ddbTableName = 'SiteCounter'
table = dynamodb.Table(ddbTableName)


def lambda_handler(event, context):
    # Update item in table or add if doesn't exist
    ddbResponse = table.update_item(
        Key={
            'id': 'count'
        },
        UpdateExpression='SET visitor_count = visitor_count + :incr',
        ExpressionAttributeValues={
            ':incr':1
        },
        ReturnValues="UPDATED_NEW"
    )


    # Format dynamodb response into variable
    responseBody = json.dumps({"count": int(ddbResponse["Attributes"]["visitor_count"])})


    # Create api response object
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": responseBody
    }


    # Return api response object

    return apiResponse