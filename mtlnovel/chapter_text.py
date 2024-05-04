import json

def extract_permalink_keys(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            permalink_keys = [item['permalink'] for item in data['items']]
            return permalink_keys
    except FileNotFoundError:
        print(f"File '{file_path}' not found")
        return []
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return []

file_path = "bulgarian empire vol 1.json"  # Replace with the path to your JSON file
permalink_keys = extract_permalink_keys(file_path)
print("Permalink keys:")
for key in permalink_keys:
    print(key)