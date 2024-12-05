import re

def main():
    with open('input.txt', 'r') as file:
        # Combine all lines into a single string
        combined_input = "".join(file.readlines()).replace("\n", "")
        
    # Calculate the total sum from the combined input
    total_sum = process_combined_input(combined_input)
    print("Total Sum:", total_sum)

def process_combined_input(corrupted_memory):
    # Regex for valid mul(X, Y)
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    # Regex for do() and don't()
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    enabled = True  # Start with mul enabled
    total_sum = 0  # Initialize the total sum

    # Tokenize by splitting valid patterns
    tokens = re.split(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", corrupted_memory)
    
    for token in tokens:
        token = token.strip()  # Clean the token
        
        if re.fullmatch(do_pattern, token):
            enabled = True  # Enable mul instructions
        elif re.fullmatch(dont_pattern, token):
            enabled = False  # Disable mul instructions
        elif re.fullmatch(mul_pattern, token):
            if enabled:
                # Extract numbers from the mul instruction
                x, y = map(int, re.findall(r"\d{1,3}", token))
                total_sum += x * y  # Add the product to the sum

    return total_sum
main()