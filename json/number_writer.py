from pathlib import Path
import json

numbers = [2, 9, 7, 4, 19, 24]
path = Path("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)