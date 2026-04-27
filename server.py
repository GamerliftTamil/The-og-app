from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Save user data to a file
def save_user(data):
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except:
        users = []

    users.append(data)

    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json

    user = {
        "username": data.get("username"),
        "password": data.get("password"),
        "ip": request.remote_addr,
        "time": str(datetime.now())
    }

    save_user(user)

    return jsonify({"message": "User registered successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
