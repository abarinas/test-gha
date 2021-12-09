import sys

def handler(event, context):
    return 'Hello aws-ecr-5 from AWS Lambda using Python ' + sys.version + '!'
