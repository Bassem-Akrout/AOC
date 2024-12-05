import random

def generate_valid_sequence(length, increasing=True):
    """
    Generate a valid sequence of specified length.
    The sequence will be strictly increasing or decreasing
    with differences between adjacent levels of 1 to 3.
    """
    sequence = [random.randint(10, 100)]  # Start with a random number
    for _ in range(length - 1):
        step = random.randint(1, 3)
        if increasing:
            sequence.append(sequence[-1] + step)
        else:
            sequence.append(sequence[-1] - step)
    return sequence

def generate_almost_valid_sequence(length):
    """
    Generate an almost valid sequence that can be made valid
    by removing one element. Insert a 'bad' value in a valid sequence.
    """
    # Start with a valid sequence
    sequence = generate_valid_sequence(length, increasing=random.choice([True, False]))
    # Insert a 'bad' level by breaking the difference rule
    index = random.randint(1, len(sequence) - 2)
    sequence[index] += random.randint(-10, 10)  # Ensure a large difference
    return sequence

def generate_test_data(lines=10, length_range=(5, 20)):
    """
    Generate test data with a mix of valid and almost valid sequences.
    """
    test_data = []
    for _ in range(lines):
        sequence_length = random.randint(*length_range)
        if random.random() < 0.7:  # 70% chance to generate valid sequences
            sequence = generate_valid_sequence(sequence_length, increasing=random.choice([True, False]))
        else:  # 30% chance to generate almost valid sequences
            sequence = generate_almost_valid_sequence(sequence_length)
        test_data.append(" ".join(map(str, sequence)))
    return test_data

# Generate test data
test_data = generate_test_data(lines=100000, length_range=(15, 200))

# File path to save the data
file_path = "inputtest.txt"

# Write test data to file
with open(file_path, "w") as file:
    for line in test_data:
        file.write(line + "\n")

print(f"Test data written to {file_path}")
