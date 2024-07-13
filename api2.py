from flask import Flask, jsonify
from flask_cors import CORS
from dronekit import connect, VehicleMode
import dronekit_sitl
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for your Flask app

# Start the Software In The Loop (SITL)
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

# Connect to the vehicle
print("Connecting to vehicle on: %s" % connection_string)
vehicle = connect(connection_string, wait_ready=True)

# Function to gather telemetry data
# Function to gather telemetry data
def gather_telemetry():
    # Get the current telemetry values
    location = {
        'latitude': vehicle.location.global_relative_frame.lat,
        'longitude': vehicle.location.global_relative_frame.lon,
        'altitude': vehicle.location.global_relative_frame.alt
    }
    speed = vehicle.groundspeed
    battery = vehicle.battery.level

    telemetry_data = {
        "location": location,
        "speed": speed,
        "battery": battery
    }
    return telemetry_data


# Route to get telemetry data
@app.route('/api/telemetry', methods=['GET'])
def get_telemetry():
    telemetry = gather_telemetry()
    return jsonify(telemetry)

# Callback function for attitude updates
def attitude_callback(self, attr_name, value):
    print(gather_telemetry())

# Add attitude listener
print("Adding telemetry listener")
vehicle.add_attribute_listener('attitude', attitude_callback)

try:
    # Run the Flask app in a separate thread
    import threading
    threading.Thread(target=lambda: app.run(debug=True, use_reloader=False)).start()

    # Keep main thread running for telemetry callback
    while True:
        time.sleep(1)

finally:
    # Clean up
    print("Removing telemetry listener")
    vehicle.remove_attribute_listener('attitude', attitude_callback)
    vehicle.close()
    sitl.stop()
    print("Simulation complete")
