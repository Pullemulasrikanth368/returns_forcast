import os
import json
import re

def load_field_mapping(screen_name):
    base_path = os.path.join("database", "field_mappings")
    screen_name_lower = screen_name.lower()
    available_files = {f.lower(): f for f in os.listdir(base_path) if f.endswith(".json")}
    target_file = f"{screen_name_lower}.json"

    if target_file not in available_files:
        raise FileNotFoundError(f"No mapping file found for screen: {screen_name}")

    file_path = os.path.join(base_path, available_files[target_file])
    with open(file_path, "r") as f:
        return json.load(f)

def map_header_to_field(screen_name, user_input):
    mapping = load_field_mapping(screen_name)
    mapped_fields = []

    for field in mapping.get(screen_name, []):
        header_name = field.get("Header", "")
        db_name = field.get("Name", "")
        if re.search(header_name, user_input, re.IGNORECASE):
            mapped_fields.append(db_name)

    return mapped_fields or [f["Name"] for f in mapping.get(screen_name, [])]
