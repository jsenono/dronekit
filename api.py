from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS from flask_cors module
from your_module import generate_random_values  # Import function for generating values
from telemetry_data import gather_telemetry

app = Flask(__name__)
CORS(app)  # Enable CORS for your Flask app

@app.route('/get-values', methods=['GET'])
def get_values():
    # Call function to get the current values
    values = generate_random_values()
    data=gather_telemetry()

    # Return the values as JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
