from flask import Flask, jsonify

app = Flask(__name__)

# Simulated data
logs = [
    "Connecting to vehicle on: tcp:127.0.0.1:5760",
    "Basic pre-arm checks",
    "Waiting for vehicle to initialise...",
    "Arming motors",
    "Taking off!",
    "Altitude: 1",
    "Altitude: 2",
    "Altitude: 3",
    "Reached target altitude",
    "Returning to Launch",
    "Close vehicle object"
]

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True)
