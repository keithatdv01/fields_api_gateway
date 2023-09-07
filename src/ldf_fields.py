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

def dlc_tags_data():
    return {
        "0":
            {
                "ds_all": ["all"],
                "ds_all_tag1": ["all", "tag1"],
                "ds_all_tag2": ["all", "tag2"],
                "ds_all_tag1_tag2": ["all", "tag1", "tag2"]
            }}

def ldf_fields_version_dataset(version: str, dataset_id: str):
    dlc_fields = dlc_tags_data()
    versioned_tags = dlc_fields.get(version)
    if versioned_tags is None:
        raise ValueError(f"Unknown LDF version: {version}")
    else:
        print(f"Tags for LDF v{version} are {versioned_tags}")
        fields_for_tags = versioned_tags.get(dataset_id)
        if fields_for_tags is None:
            raise ValueError(f"Unknown tags: {dataset_id}")
        else:
            return fields_for_tags
