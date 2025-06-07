# Pet Application

This repository contains a simple command line application for managing pets and users.

## Modules

- **`pet_app/pets.py`** - functions to add and list pets using a JSON file for storage.
- **`pet_app/users.py`** - user registration and listing logic.
- **`pet_app/adoption.py`** - records pet adoptions.
- **`pet_app/services.py`** - extra services like calculating adoption fees.
- **`pet_app/main.py`** - CLI entry point to interact with the system.
- **`pet_app/web.py`** - simple Flask web application exposing API endpoints.

## Running the app

Ensure you have Python 3 installed. Execute commands using the module:

```bash
python -m pet_app.main <command> [options]
```

Examples:

```bash
python -m pet_app.main add-pet Rex dog 2
python -m pet_app.main list-pets
python -m pet_app.main add-user Alice
```

All data is stored in JSON files inside the `pet_app` directory.

### Web API

Install Flask and run the web application:

```bash
pip install flask
python -m pet_app.web
```

The server exposes JSON endpoints at `/pets`, `/users`, and `/adopt`.
