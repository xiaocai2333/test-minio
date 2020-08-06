import os
from minio import Minio
from minio.error import (ResponseError,
                         BucketAlreadyExists,
                         BucketAlreadyOwnedByYou,
                         NoSuchKey)

if __name__ == "__main__":
    minio_client2 = Minio('127.0.0.1:9000',
                          access_key='Thylanine',
                          secret_key='Thylacine',
                          secure=False)
    minio_client1 = Minio('play.min.io',
                          access_key='Q3AM3UQ867SPQQA43P2F',
                          secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                          secure=True)
    # print("**************list buckets******************")
    # buckets = minio_client2.list_buckets()
    # for bucket in buckets:
    #     print(bucket.name)

    print("**************enable version******************")
    minio_client2.disable_bucket_versioning("zcbucket")

    print("**************put objects******************")
    for i in range(10):
        file_stat = os.stat('hello.txt')
        with open('hello.txt', 'rb') as data:
            minio_client2.put_object(
                'zcbucket', 'bar' + str(i), data, file_stat.st_size, 'text/plain',
            )

    print("**************fput objects******************")
    minio_client2.fput_object("zcbucket", "readme.md", "./README.md")

    print("**************list objects******************")
    objects = minio_client2.list_objects(bucket_name="zcbucket", include_version=False)
    for object in objects:
        print(object.object_name)
        print(object.version_id)

    print("***************list objects_v2*****************")
    objects = minio_client2.list_objects_v2(bucket_name="zcbucket", prefix="bar", include_version=False)
    for object in objects:
        print(object.object_name)
        print(object.version_id)

    print("***************list objects_v2*****************")
    objects = minio_client2.list_objects_v2(bucket_name="zcbucket", prefix="bar", recursive=False)
    for object in objects:
        print(object.object_name)
        print(object.version_id)

    print("***************list objects_v2*****************")
    objects = minio_client2.list_objects_v2(bucket_name="zcbucket",
                                            prefix="ba",
                                            recursive=False,
                                            start_after="ba",
                                            include_version=False)
    for object in objects:
        print(object.object_name)
        print(object.version_id)
        print(object.metadata)

    print("***************get object*****************")
    object = minio_client2.get_object(bucket_name="zcbucket", object_name="bar",
                                      version_id="26a34677-5c0f-45cc-b1d8-13fbc265f6c5")
    print(object.data)

    object = minio_client2.get_object(bucket_name="zcbucket", object_name="bar",
                                      version_id="fd3bfab5-a2b2-4a78-8d37-9a261e9b908d")
    print(object.data)

    print("***************remove object*****************")
    minio_client2.remove_object("zcbucket", "bar")

    print("***************get object*****************")
    try:
        object = minio_client2.get_object(bucket_name="zcbucket", object_name="bar",
                                      )
    except NoSuchKey as err:
        print("key bar is not exist!")
    print(object.data)

    object = minio_client2.get_object(bucket_name="zcbucket", object_name="bar",
                                      version_id="fd3bfab5-a2b2-4a78-8d37-9a261e9b908d")
    print(object.data)

    print("***************remove objects*****************")
    objects = minio_client2.list_objects_v2(bucket_name="zcbucket",
                                            prefix="ba",
                                            recursive=False,
                                            start_after="ba",
                                            include_version=False)
    status = minio_client2.remove_objects("zcbucket", [object.object_name for object in objects])
    # print(list(status))

    print("***************list objects*****************")
    objects = minio_client2.list_objects(bucket_name="zcbucket", include_version=False)
    for object in objects:
        print(object.object_name)