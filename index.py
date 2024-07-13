from collections.abc import MutableMapping
from dronekit import connect, VehicleMode

# Connect to the Vehicle
connection_string = '127.0.0.1:14550'
print(f'Connecting to vehicle on: {connection_string}')
vehicle = connect(connection_string, wait_ready=True)

# Function to display GPS information
def gps_callback(self, attr_name, value):
    print(f"GPS: {value}")

# Function to display battery status
def battery_callback(self, attr_name, value):
    print(f"Battery: {value}")

# Function to display attitude (orientation) information
def attitude_callback(self, attr_name, value):
    print(f"Attitude: {value}")

# Add listeners for telemetry data
vehicle.add_attribute_listener('gps_0', gps_callback)
vehicle.add_attribute_listener('battery', battery_callback)
vehicle.add_attribute_listener('attitude', attitude_callback)

print("Vehicle is ready")

# Allow the script to run for a while to receive data
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

# Close the vehicle connection
vehicle.close()
print("Connection closed")
