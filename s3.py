import boto3

s3 = boto3.client('s3')

s3.upload_file('s3_transfer.txt', 'jyoharikow', 's3_file1.txt')

