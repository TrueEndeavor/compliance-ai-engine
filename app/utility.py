import json
from typing import Optional

def load_json_file(file_path: str) -> Optional[str]:

    try:
        with open(file_path, 'r', encoding='utf-8') as file:

            data = json.load(file)
            return json.dumps(data, indent=2)
    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None

def load_text_file(file_path: str) -> Optional[str]:
    try:
        with open(file_path, 'r', encoding='UTF-8') as file:
            return file.read()
        
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None

