import boto3


class S3Client:
    def __init__(self, s3):
        self.s3 = s3

    def download_file(self, bucket_name, key, file_path):
        self.s3.download_file(bucket_name, key, file_path)

    def write_to_s3(self, bucket_name, key, data):
        self.s3.put_object(Bucket=bucket_name, Key=key, Body=data)
