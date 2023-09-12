import random

def validate_input(input_str, data_type):
    try:
        if data_type == "number":
            numbers = [int(num.strip()) for num in input_str.split(",")]
        elif data_type == "string":
            strings = [str(s.strip()) for s in input_str.split(",")]
        return True
    except ValueError:
        return False

def generate_random_array(size):
    return [random.randint(-1000, 1000) for _ in range(size)]
