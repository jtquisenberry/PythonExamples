# https://stackoverflow.com/questions/50100221/download-file-from-aws-s3-using-python

import boto3

s3 = boto3.client('s3', aws_access_key_id='AKIAVQHTBMWH3U4FCEGQ' , aws_secret_access_key='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')
s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')

