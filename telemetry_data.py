from dronekit import connect, VehicleMode
import time

# Start the Software In The Loop (SITL)
import dronekit_sitl

# Start SITL and get connection string
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

# Connect to the vehicle
print("Connecting to vehicle on: %s" % connection_string)
vehicle = connect(connection_string, wait_ready=True)

# Function to gather telemetry data
def gather_telemetry():
    telemetry_data = {
        "location": vehicle.location.global_relative_frame,
        "speed": vehicle.groundspeed,
        "battery": vehicle.battery.level
    }
    return telemetry_data

# Callback function for attitude updates
def attitude_callback(self, attr_name, value):
    print(gather_telemetry())

# Add attitude listener
print("Adding telemetry listener")
vehicle.add_attribute_listener('attitude', attitude_callback)

try:
    # Print telemetry for 10 seconds
    time.sleep(10)

finally:
    # Clean up
    print("Removing telemetry listener")
    vehicle.remove_attribute_listener('attitude', attitude_callback)
    vehicle.close()
    sitl.stop()
    print("Simulation complete")
