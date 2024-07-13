from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

def get_dummy_data():
    result = subprocess.run(['python', 'dummy_data.py'], capture_output=True, text=True)
    logs = result.stdout.split('\n')
    return [log for log in logs if log]  # Remove any empty strings

@app.route('/logs', methods=['GET'])
def get_logs():
    logs = get_dummy_data()
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True)
