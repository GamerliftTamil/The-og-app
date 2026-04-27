from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

USER_FILE = "users.json"


# Serve frontend page
@app.route("/")
def home():
    return render_template("index.html")


def load_users():
    try:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
@app.route("/users", methods=["GET"])
def get_users():
    users = load_users()
    return jsonify(users)
    if not data:
        return jsonify({"error": "No data provided"}), 400

    username = data.get("username")
    email = data.get("email")

    if not username or not email:
        return jsonify({"error": "Username and email are required"}), 400

    users = load_users()

    user = {
        "username": username,
        "email": email,
        "ip": request.remote_addr
    }

    users.append(user)
    save_users(users)

    return jsonify({
        "message": "User registered successfully ✅",
        "user": user
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
