# Generate a random device ID using uuid.
import uuid
def generate_random_device_id():
    return str(uuid.uuid4())

print(generate_random_device_id())