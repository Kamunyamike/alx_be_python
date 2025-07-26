import json
def process_json(data: dict, filename: str) -> dict:
    # Serialize (write) the dictionary to a JSON file
    with open(filename, 'w') as file:
        json.dump(data, file)

    # Deserialize (read) the JSON file back into a dictionary
    with open(filename, 'r') as file:
        deserialized_data = json.load(file)

    return deserialized_data

my_data = {"name": "Alice", "age": 30, "is_student": False}
file_name = "person.json"

result = process_json(my_data, file_name)
print(result)
