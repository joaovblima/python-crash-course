from pathlib import Path
import json

path = Path("number.json")
number = int(input("digite um numero: "))
content = json.dumps(number)
path.write_text(content)
