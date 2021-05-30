from google.cloud import storage as gcs
from google.oauth2 import service_account

key_path = "key/gcs-access.json"
gcs_path = "tensorflow/test.png"
credential = service_account.Credentials.from_service_account_file(key_path)


def delete_image(project_id: str, bucket_name: str) -> None:

    client = gcs.Client(project_id, credentials=credential)
    bucket = client.bucket(bucket_name)
    blob_gcs = bucket.blob(gcs_path)

    try:
        blob_gcs.delete()
        print(f"{gcs_path} in gs://{bucket_name} is deleted.")

    except:
        print("There is no test.png")
