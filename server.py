from flask import Flask, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/save', methods=['POST'])
def save():
    data = request.json

    name = data.get("name")
    email = data.get("email")

    with open("userdata.txt", "a") as file:
        file.write(f"Name: {name}, Email: {email}\n")

    return "Data saved successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
