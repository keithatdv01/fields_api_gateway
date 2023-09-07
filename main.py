from fastapi import FastAPI
from src.ldf_fields import ldf_fields_data, ldf_fields_version_tags, ldf_fields_version_dataset

app = FastAPI()

# FIXME: handle errors

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/version")
def get_api_internal_version():
    return {"version": "0.0.1"}

# Get all LDF fields for a given version
@app.get("/ldf_fields/{version}")
def get_ldf_fields_version(version: str):
    print(ldf_fields_data())
    return {"version": version,
            "fields": ["field1", "field2", "field3"]}

# Get all LDF fields for a given version and DLC tags/scope
# TODO: use query parameters for tags
# TODO: support multiple tags and union results
@app.get("/ldf_fields/{version}/tags/{tags}")
def get_ldf_fields_version_tags(version: str, tags: str):
    print("got tags: ", tags)
    return ldf_fields_version_tags(version, tags)

# Get all LDF fields for a given version and dataset from DLC
# TODO: use query parameters for dataset ID
@app.get("/ldf_fields/{version}/dataset/{dataset_id}")
def get_ldf_fields_version_dataset(version: str, dataset_id: str):
    print("got tags: ", dataset_id)
    return ldf_fields_version_dataset(version, dataset_id)
