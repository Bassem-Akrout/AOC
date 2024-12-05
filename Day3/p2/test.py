import re

def main():
    total_sum = 0  # Initialize total sum
    enabled = True  # At the start, mul instructions are enabled
    
    with open('input.txt', 'r') as file:  # Open the input file
        for line in file:  # Iterate over each line
            summ,enabled=explore_str(line, enabled) 
            total_sum += summ # Process each line
            
    print(total_sum)  # Output the total sum

def explore_str(corrupted_memory, initial_state):
    # Patterns for do(), don't(), and mul(X,Y)
    print("start",initial_state)
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    enabled = initial_state  # Use the initial state passed to the function
    total_sum = 0  # Initialize sum for this string

    # Tokenize the string into sequential instructions
    tokens = re.split(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", corrupted_memory)
    
    for token in tokens:
        token = token.strip()
        # Skip tokens that are not do(), don't(), or mul()
        if not (re.fullmatch(do_pattern, token) or re.fullmatch(dont_pattern, token) or re.fullmatch(mul_pattern, token)):
            continue  # Skip invalid tokens
        
        # Handle do() instruction
        if re.fullmatch(do_pattern, token):
            enabled = True  # Enable mul instructions
        
        # Handle don't() instruction
        elif re.fullmatch(dont_pattern, token):
            enabled = False  # Disable mul instructions
        
        # Handle mul() instruction
        elif re.fullmatch(mul_pattern, token):
            if enabled:
                # Extract numbers from the mul instruction
                x, y = map(int, re.findall(r"\d{1,3}", token))
                
                total_sum += x * y  # Add the product to the sum
            else:
                # Extract numbers from the mul instruction
                x, y = map(int, re.findall(r"\d{1,3}", token))
                
    initial_state=enabled
    print("end",enabled)
    return total_sum,enabled

if __name__ == "__main__":
    main()
