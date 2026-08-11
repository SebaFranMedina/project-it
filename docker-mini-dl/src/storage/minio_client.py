from minio import Minio
from pathlib import Path
from io import BytesIO
import pandas as pd
import json


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def get_client():
    return Minio(
        "minio:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False,
    )


def upload_file(bucket_name: str, file_path: str, object_name: str | None = None):

    client = get_client()

    file_path = PROJECT_ROOT / file_path

    if object_name is None:
        object_name = file_path.name

    client.fput_object(
        bucket_name=bucket_name,
        object_name=object_name,
        file_path=str(file_path)
    )

    print(f"Archivo '{object_name}' subido correctamente al bucket '{bucket_name}'.")


def read_csv(bucket_name: str, object_name: str):

    client = get_client()

    response = client.get_object(
        bucket_name=bucket_name,
        object_name=object_name
    )

    try:
        data = response.read()

        df = pd.read_csv(BytesIO(data))

        return df

    finally:
        response.close()
        response.release_conn()

def upload_bytes(
    bucket_name: str,
    object_name: str,
    data: bytes,
    content_type: str
):
    client = get_client()

    client.put_object(
        bucket_name=bucket_name,
        object_name=object_name,
        data=BytesIO(data),
        length=len(data),
        content_type=content_type
    )

    print(
        f"Archivo '{object_name}' "
        f"subido correctamente al bucket '{bucket_name}'."
    )

def upload_json(
    bucket_name: str,
    object_name: str,
    data: dict
):
    client = get_client()

    json_data = json.dumps(
        data,
        ensure_ascii=False
    ).encode("utf-8")

    client.put_object(
        bucket_name=bucket_name,
        object_name=object_name,
        data=BytesIO(json_data),
        length=len(json_data),
        content_type="application/json"
    )

def read_parquet(bucket_name: str, object_name: str):

    client = get_client()

    response = client.get_object(
        bucket_name=bucket_name,
        object_name=object_name
    )

    try:
        data = response.read()

        df = pd.read_parquet(BytesIO(data))

        return df

    finally:
        response.close()
        response.release_conn()


def read_json(bucket_name: str, object_name: str):

    client = get_client()

    response = client.get_object(
        bucket_name=bucket_name,
        object_name=object_name
    )

    try:
        data = response.read()

        return json.loads(data.decode("utf-8"))

    finally:
        response.close()
        response.release_conn()