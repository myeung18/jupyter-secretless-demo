import boto3


def s3_client():
    s3 = boto3.client('s3')
    return s3


def list_buckets():
    bck_rep = s3_client().list_buckets()
    for buck in bck_rep["Buckets"]:
        print(buck)


if __name__ == '__main__':
    print(list_buckets())
