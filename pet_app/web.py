from flask import Flask, jsonify, request
from .pets import add_pet, list_pets
from .users import add_user, list_users
from .adoption import adopt_pet

app = Flask(__name__)


@app.route("/pets", methods=["GET", "POST"])
def pets_endpoint():
    if request.method == "POST":
        data = request.get_json() or {}
        pet = add_pet(data.get("name"), data.get("species"), int(data.get("age", 0)))
        return jsonify(pet), 201
    else:
        return jsonify(list_pets())


@app.route("/users", methods=["GET", "POST"])
def users_endpoint():
    if request.method == "POST":
        data = request.get_json() or {}
        user = add_user(data.get("name"))
        return jsonify(user), 201
    else:
        return jsonify(list_users())


@app.route("/adopt", methods=["POST"])
def adopt_endpoint():
    data = request.get_json() or {}
    adoption = adopt_pet(int(data.get("pet_id", 0)), int(data.get("user_id", 0)))
    return jsonify(adoption), 201


if __name__ == "__main__":
    app.run(debug=True)
