import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "db_users.json"


def load_users():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=2)


def add_user(name: str):
    users = load_users()
    user_id = max([u.get("id", 0) for u in users], default=0) + 1
    user = {"id": user_id, "name": name}
    users.append(user)
    save_users(users)
    return user


def list_users():
    return load_users()
