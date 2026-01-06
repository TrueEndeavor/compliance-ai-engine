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

def clean_and_parse_json(raw):
    if raw is None:
        return None

    if isinstance(raw, dict):
        return raw

    if isinstance(raw, str):
        raw = raw.strip()
        if raw.startswith("```"):
            raw = raw.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {
                "error": "LLM returned invalid JSON",
                "raw_output": raw
            }

    return {
        "error": "Unexpected data type",
        "raw_output": str(raw)
    }