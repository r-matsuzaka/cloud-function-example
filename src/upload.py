from google.cloud import storage as gcs
from google.oauth2 import service_account

key_path = "key/gcs-access.json"
gcs_path = "tensorflow/test.png"
local_path = "data/test.png"


def upload(project_id: str, bucket_name: str) -> None:
    credential = service_account.Credentials.from_service_account_file(key_path)
    client = gcs.Client(project_id, credentials=credential)
    bucket = client.get_bucket(bucket_name)
    blob_gcs = bucket.blob(gcs_path)
    blob_gcs.upload_from_filename(local_path)

    print(f"Uploading {local_path} to gs://{bucket_name} is finished.")
