import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "db_adoptions.json"


def load_adoptions():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_adoptions(adoptions):
    with open(DATA_FILE, "w") as f:
        json.dump(adoptions, f, indent=2)


def adopt_pet(pet_id: int, user_id: int):
    adoptions = load_adoptions()
    adoption_id = max([a.get("id", 0) for a in adoptions], default=0) + 1
    adoption = {"id": adoption_id, "pet_id": pet_id, "user_id": user_id}
    adoptions.append(adoption)
    save_adoptions(adoptions)
    return adoption
