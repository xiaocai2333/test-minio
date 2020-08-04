from minio import Minio
from minio.error import (ResponseError,
                         BucketAlreadyExists,
                         BucketAlreadyOwnedByYou)

minio_client = Minio('play.min.io',
                  access_key='Q3AM3UQ867SPQQA43P2F',
                  secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                  secure=True)

try:
    minio_client.make_bucket("zcbucket1", location="us-east-1")
except BucketAlreadyOwnedByYou as err:
    print("BucketAlreadyOwnedByYou")
    pass
except BucketAlreadyExists as err:
    print("BucketAlreadyExists")
    pass
except ResponseError as err:
    print("ResponseError")
    raise
else:
    try:
        minio_client.fput_object('zcbucket1', 'README.md', './README.md')
    except ResponseError as err:
        print(err)