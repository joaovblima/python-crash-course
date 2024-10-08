from pathlib import Path
import json

path = Path("number.json")
if path.exists:
    content = path.read_text()
    number = json.loads(content)
    print(f"EU sei que seu numero preferido eh {number}")