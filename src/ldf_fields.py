def ldf_fields_data():
    return {
        "0":
            {"fields":
                 {"all": ["field0"],
                  "tag1": ["field1", "field2"],
                  "tag2": ["field3", "field4"]}}}


def ldf_fields_version_tags(version: str, tags: str):
    tagged_fields = ldf_fields_data()
    versioned_fields = tagged_fields.get(version)
    if versioned_fields is None:
        raise ValueError(f"Unknown LDF version: {version}")
    else:
        print(f"tagged fields for v{version} are {versioned_fields}")
        fields_for_tags = versioned_fields.get("fields").get(tags)
        if fields_for_tags is None:
            raise ValueError(f"Unknown tags: {tags}")
        else:
            return fields_for_tags
