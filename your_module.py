import random
from telemetry_data import gather_telemetry

def generate_random_values():
    data=gather_telemetry()
    value1 = random.randint(1, 100)
    value2 = random.choice(['Hello', 'World', 'Flask'])
    values = {
        'value1': value1,
        'value2': value2
    }
    print(data)
    
    return values