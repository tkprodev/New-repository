import argparse
from .pets import add_pet, list_pets
from .users import add_user


def main():
    parser = argparse.ArgumentParser(description="Pet App CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add pet
    add_pet_parser = subparsers.add_parser("add-pet", help="Register a new pet")
    add_pet_parser.add_argument("name")
    add_pet_parser.add_argument("species")
    add_pet_parser.add_argument("age", type=int)

    # List pets
    subparsers.add_parser("list-pets", help="List all pets")

    # Add user
    add_user_parser = subparsers.add_parser("add-user", help="Register a new user")
    add_user_parser.add_argument("name")

    args = parser.parse_args()

    if args.command == "add-pet":
        pet = add_pet(args.name, args.species, args.age)
        print(f"Added pet: {pet}")
    elif args.command == "list-pets":
        pets = list_pets()
        for pet in pets:
            print(f"{pet['id']}: {pet['name']} ({pet['species']}, {pet['age']} years old)")
    elif args.command == "add-user":
        user = add_user(args.name)
        print(f"Added user: {user}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
