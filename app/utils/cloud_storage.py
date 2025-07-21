import os
import tempfile
import boto3
from botocore.exceptions import ClientError

class CloudStorage:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_REGION', 'us-east-1')
        )
        self.bucket_name = os.getenv('AWS_BUCKET_NAME')

    def download_file(self, s3_key, local_path):
        try:
            self.s3_client.download_file(self.bucket_name, s3_key, local_path)
            return True
        except ClientError as e:
            print(f"Error downloading file: {e}")
            return False

    def upload_file(self, local_path, s3_key):
        try:
            self.s3_client.upload_file(local_path, self.bucket_name, s3_key)
            return True
        except ClientError as e:
            print(f"Error uploading file: {e}")
            return False

    def get_temp_file_path(self):
        temp_dir = tempfile.gettempdir()
        return os.path.join(temp_dir, 'temp_faiss_index')
