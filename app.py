from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Chess Learning Platform API is live!"})

if __name__ == '__main__':
    app.run(debug=True)
