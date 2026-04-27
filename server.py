from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
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
        "email": data.get("email"),
        "ip": request.remote_addr,
    }

    save_user(user)

    return jsonify({"message": "User registered successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
