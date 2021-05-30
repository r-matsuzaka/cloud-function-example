from src import delete_image
from src import prepare_image
from src import upload
from src import request
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--project_id")
parser.add_argument("--bucket_name")
parser.add_argument("--trigger")

args = parser.parse_args()


delete_image.delete_image(project_id=args.project_id, bucket_name=args.bucket_name)

prepare_image

upload.upload(project_id=args.project_id, bucket_name=args.bucket_name)

request.requests(trigger=args.trigger)
