from fastapi import FastAPI
from src.ldf_fields import ldf_fields_data, ldf_fields_version_tags

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/version")
def maggyar_version():
    return {"version": "0.0.1"}

# generate code to define API methods here for the following:
# - get all LDF fields for a given version

@app.get("/ldf_fields/{version}")
def get_ldf_fields(version: str):
    print(ldf_fields_data())
    return {"version": version,
            "fields": ["field1", "field2", "field3"]}

# - get all LDF fields for a given version and DLC tags/scope
@app.get("/ldf_fields/{version}/{tags}")
def get_ldf_fields(version: str, tags: str):
    print("got tags: ", tags)
    return ldf_fields_version_tags(version, tags)
