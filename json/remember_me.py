from pathlib import Path
import json



def get_stored_user(path):
    if path.exists():
        content = path.read_text()
        user = json.loads(content)
        return user
    else:
        None


def get_new_username(path):
    info_user = {}
    username = input("Whats your name? ")
    age = input("Your age? ")
    city = input("Your city? ")
    info_user["name"] = username
    info_user["age"] = age
    info_user["city"] = city
    content = json.dumps(info_user)
    path.write_text(content)
    return info_user


def great_user():
    path = Path("username.json")
    user = get_stored_user(path)
    if user:
        print(f"Welcome back, {user['name']}")
    else:
        username = get_new_username(path)
        print(f"well remember you when you come back, {user['name']}")

great_user()