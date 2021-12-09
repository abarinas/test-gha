import sys

def handler(event, context):
    return 'Hello  aws-ecr-3 from AWS Lambda using Python ' + sys.version + '!'
