def parse(path):
    # Open the file and read the lines
    with open(path, 'r') as file:
        order_rules = {}  # Store ordering rules as a dictionary of sets
        updates = []      # List to store updates

        # Process each line in the file
        for line in file:
            if '|' in line:
                # Parse ordering rules
                x, y = map(int, line.strip().split('|'))
                if x not in order_rules:
                    order_rules[x] = set()
                order_rules[x].add(y)
            else:
                try:
                    # Parse updates
                    updates.append(list(map(int, line.strip().split(','))))
                except ValueError:
                    continue
    
    return order_rules, updates

def is_valid_update(order_rules, update):
    # Check if an update is valid according to the rules
    n = len(update)
    for i in range(n):
        x = update[i]
        for j in range(i + 1, n):  # Triangular loop: check forward pairs
            y = update[j]
            if y in order_rules and x in order_rules[y]:  # Check if x is in y's rules
                return False  # Rule violated
    return True
def calculate_middle_page_sum(order_rules, updates):
    total_sum = 0
    for update in updates:
        if is_valid_update(order_rules, update):
            # Find the middle page number
            middle_index = len(update) // 2
            total_sum += update[middle_index]
    return total_sum

def main():
    # Path to the input file
    input_path = "input.txt"  # Replace with your file path

    # Parse the input data
    order_rules, updates = parse(input_path)

    # Calculate the sum of middle page numbers for valid updates
    result = calculate_middle_page_sum(order_rules, updates)

    print("Sum of middle page numbers for valid updates:", result)

if __name__=="__main__":
    main()