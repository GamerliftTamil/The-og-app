from flask import Flask, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')
from flask import send_file

@app.route('/download')
def download_file():
    return send_file("userdata.txt", as_attachment=True)    

@app.route('/save', methods=['POST'])
def save():
    data = request.json

    name = data.get("name")
    email = data.get("email")

    with open("userdata.txt", "a") as file:
        file.write(f"Name: {name}, Email: {email}\n")

    return "Data saved successfully(I'm the danger!!)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
