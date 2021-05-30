# cloud-function-example
This is a toy example code for cloud function using fashion MNIST.

# Feature
You upload a fashion MNIST image, which is randomly chosen from test dataset, to Cloud storage(GCS) for inference.
Pretrained model is also set in GCS.
You request Cloud Functions as http requests to get the inference result.
You will get the status code and inference code like this in your command .


```
Test image[9369] is created!
tensorflow/test.png in gs://tfserving1 is deleted.
Uploading data/test.png to gs://tfserving1 is finished.
200
Bag
```

# Install
At loacal, run `poetry install`.

# How to use
1. Create trained model
```
cd src
python3 train.py
```
Then you will get `fashion_mnist_weights.data-00000-of-00001` and `fashion_mnist_weights.index`.
Those files are put in CLoud Storage.


2. Prepare GCP environment

In this example, you use 2 GCP services which are Cloud Storage(GCS) and Cloud Functions.
Thre is a free tier for new user for GCP.
This toy program can be use within it.


- GCS
In Cloud storage bucket you need to prepare directories as follows.
In tensorflow directory, please put files which are created at previous step as follows.

├── tensorflow
│   ├── fashion_mnist_weights.data-00000-of-00001
│   └── fashion_mnist_weights.index
└── tmp

Next you need to get credential key to access to GCP bucket from local.
At `upload.py` process. you upload `test.png` in tensorflow directory in GCS.

Open Google command line tool in GCP,

Then run this commands. Please fill your project id at {project_id}.
You don't need {}.

```
gcloud iam service-accounts create gcs-access

gcloud projects add-iam-policy-binding {project_id} --member=serviceAccount:gcs-access@{project_id}.iam.gserviceaccount.com --role="roles/storage.admin"

cloud iam service-accounts keys create gcs-access.json --iam-account gcs-access@{project_id}.iam.gserviceaccount.com
```

Then, you will get a credential key as "gcs-access.json", please copy it in your key directory.
This is key to your GCS, so please keep it in private.


For More detail, see below.
[GoogleCloudStorage GCSのPythonAPIの使い方](https://qiita.com/Hyperion13fleet/items/594c15ac24f149ab73c9)
[Python クライアントライブラリで Google Cloud Storage の参照・作成・更新・削除操作をするにはどのメソッドを使えばよいのか確認してみた](https://dev.classmethod.jp/articles/gcs-python-client-libraries-how2/)
[gcloud projects add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding#PROJECT_ID)

- Cloud Functions
Please copy and paste at the `main.py` and `requirements.py` in `src/cloud-funciotns` for codes in Cloud Functions.

Setting for Cloud functions.
```
Memory:2 GB
Runtime:Python3.7
Entrypoint:handler
```
In this code example, http request is used thus permission should be added.
Navigate to permission page and choose `allUsers` for member section and `Cloud Functions Invoker`(`Cloud Functions 起動元`)for a role.
If you don't set the permission you get 403 error.
See [this site(Japanese)](https://qiita.com/toshiaki_takase/items/ce65cd5582a80917b52f) as reference.

After deploying Cloud Functions please copy trigger whose form is `http://......` to give `main.py`.
This triger can be accessed publicly because of permission setting mentioned above.
So you should not open this url to public. Cloud Functions incur chaerges based on the time you trigger Cloud Functions.

2. Run code
`python3 main.py --project_id {YOUR_PROJECT_ID} --bucket_name {YOUR_BUCKET_NAME}  --trigger {YOUR_TRIGGER}` 

# Reference

- [How to serve deep learning models using TensorFlow 2.0 with Cloud Functions](https://cloud.google.com/blog/products/ai-machine-learning/how-to-serve-deep-learning-models-using-tensorflow-2-0-with-cloud-functions)
Training code is based on this site.
