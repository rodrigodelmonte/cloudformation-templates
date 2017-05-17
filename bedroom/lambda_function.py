import boto3
import requests
import json
import os

s3 = boto3.client('s3')
bucket_name=os.environ['S3Bucket']

def lambda_handler(event, context):

    if event['RequestType'] == 'Create':

        with open('/tmp/index_on.html', 'w') as f:
            turnon = '<html><body style="background-color:#000000;"><img src="http://bit.ly/2pUPixl" ></body></html>'
            f.write(turnon)

        s3.upload_file('/tmp/index_on.html',
                        Bucket=bucket_name,
                        Key='index.html',
                        ExtraArgs={'ContentType': "text/html", 'ACL': "public-read"})

        reason = 'See the details in CloudWatch Log Stream: %s' % context.log_stream_name
        response = {"Status": 'SUCCESS',
                    "Reason": reason,
                    "PhysicalResourceId": context.log_stream_name,
                    "StackId": event['StackId'],
                    "RequestId": event['RequestId'],
                    "LogicalResourceId": event['LogicalResourceId'],
                    "Data": {'Action': 'TurnOn'} }
        headers = {
            "content-type": "",
            "content-length": str(len(response))
        }

        r = requests.put(event['ResponseURL'], data=json.dumps(response), headers=headers)
        print "Status Code: %s" % r.status_code

    elif event['RequestType'] == 'Delete':

        with open('/tmp/index_off.html', 'w') as f:
            turnoff = '<html><body style="background-color:#000000;"></body></html>'
            f.write(turnoff)

        s3.upload_file('/tmp/index_off.html',
                        Bucket=bucket_name,
                        Key='index.html',
                        ExtraArgs={'ContentType': "text/html", 'ACL': "public-read"})

        reason = 'See the details in CloudWatch Log Stream: %s' % context.log_stream_name
        response = {"Status": 'SUCCESS',
                    "Reason": reason,
                    "PhysicalResourceId": context.log_stream_name,
                    "StackId": event['StackId'],
                    "RequestId": event['RequestId'],
                    "LogicalResourceId": event['LogicalResourceId'],
                    "Data": {'Action': 'TurnOff'} }
        headers = {
            "content-type": "",
            "content-length": str(len(response))
        }

        r = requests.put(event['ResponseURL'], data=json.dumps(response), headers=headers)
        print "Status Code: %s" % r.status_code

    return response