from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

USER_FILE = "users.json"


# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Server is running "
    })


# Load users
def load_users():
    try:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    except:
        return []


# Save users
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)


# Signup route
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No data provided"
        }), 400

    username = data.get("username")
    email = data.get("email")

    if not username or not email:
        return jsonify({
            "error": "Username and email are required"
        }), 400

    users = load_users()

    user = {
        "username": username,
        "email": email,
        "ip": request.remote_addr
    }

    users.append(user)
    save_users(users)

    return jsonify({
        "message": "User registered successfully ",
        "user": user
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
