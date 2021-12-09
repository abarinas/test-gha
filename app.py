import sys

def handler(event, context):
    return 'Hello aws-ecr-7 from AWS Lambda using Python ' + sys.version + '!'
