from pathlib import Path

dog_path = Path("dogs.txt")
cat_path = Path("cats.txt")

try:
    dog_content = dog_path.read_text().split()
    cat_content = cat_path.read_text().split()
except FileNotFoundError:
    pass
else:
    print("dogs: ")
    for dog in dog_content:
        print(f"-> {dog}")
    print("cats: ")
    for cat in cat_content:
        print(f"-* {cat}")
