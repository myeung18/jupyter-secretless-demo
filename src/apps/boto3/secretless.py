import boto3
from botocore.config import Config


def s3_client():
    s3 = boto3.client('s3',
                      aws_access_key_id="secretless",
                      region_name="us-east-1",
                      aws_secret_access_key="secretless",
                      endpoint_url="http://secretless.empty",
                      config=Config(proxies={'http': 'http://localhost:8099'}))
    return s3


def list_buckets():
    bck_rep = s3_client().list_buckets()
    for buck in bck_rep["Buckets"]:
        print(buck)


def create_bucket():
    return s3_client().create_bucket(
        Bucket="polo202214"
    )


if __name__ == '__main__':
    # create_bucket()
    print(list_buckets())
