# app.py

from flask import Flask, jsonify
from simple import logs

app = Flask(__name__)

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True)
