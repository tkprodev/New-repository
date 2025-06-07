import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "db_pets.json"


def load_pets():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_pets(pets):
    with open(DATA_FILE, "w") as f:
        json.dump(pets, f, indent=2)


def add_pet(name: str, species: str, age: int):
    pets = load_pets()
    pet_id = max([p.get("id", 0) for p in pets], default=0) + 1
    pet = {"id": pet_id, "name": name, "species": species, "age": age}
    pets.append(pet)
    save_pets(pets)
    return pet


def list_pets():
    return load_pets()
