from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Chess Learning Platform API is live!"})

@app.route('/puzzles', methods=['GET'])
def get_puzzles():
    url = "https://lichess.org/api/puzzle"
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Failed to fetch puzzles"}), 500

if __name__ == '__main__':
    app.run(debug=True)
