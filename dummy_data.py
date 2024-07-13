# dummy_data.py
import time

def generate_logs():
    logs = []
    logs.append("Connecting to vehicle on: tcp:127.0.0.1:5760")
    time.sleep(1)
    logs.append("Basic pre-arm checks")
    time.sleep(1)
    logs.append("Waiting for vehicle to initialise...")
    time.sleep(1)
    logs.append("Arming motors")
    time.sleep(1)
    logs.append("Taking off!")
    for i in range(1, 4):
        logs.append(f"Altitude: {i}")
        time.sleep(1)
    logs.append("Reached target altitude")
    time.sleep(1)
    logs.append("Returning to Launch")
    time.sleep(1)
    logs.append("Close vehicle object")
    return logs

if __name__ == '__main__':
    logs = generate_logs()
    for log in logs:
        print(log)
