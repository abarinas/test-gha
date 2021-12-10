import sys

def handler(event, context):
    return 'Hello aws-ecr- from AWS Lambda using Python ' + sys.version + '!'
