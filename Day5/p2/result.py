from collections import defaultdict, deque

def parse(path):
    # Open the file and read the lines
    with open(path, 'r') as file:
        order_rules = defaultdict(set)  # Store ordering rules as a dictionary of sets
        updates = []  # List to store updates

        for line in file:
            if '|' in line:
                # Parse ordering rules
                x, y = map(int, line.strip().split('|'))
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


def reorder_update(order_rules, update):
    # Reorder an update using topological sorting
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Build the dependency graph
    for x in update:
        graph[x] = []  # Ensure every page is in the graph
    for x in update:
        if x in order_rules:
            for y in order_rules[x]:
                if y in update:  # Only consider rules for pages in this update
                    graph[x].append(y)
                    in_degree[y] += 1

    # Perform topological sorting
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []

    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update


def calculate_middle_page_sum(order_rules, updates):
    incorrect_updates = []
    corrected_middle_sum = 0

    for update in updates:
        if not is_valid_update(order_rules, update):
            # Reorder the update
            corrected_update = reorder_update(order_rules, update)
            incorrect_updates.append(corrected_update)
            # Calculate the middle page
            middle_index = len(corrected_update) // 2
            corrected_middle_sum += corrected_update[middle_index]

    return corrected_middle_sum, incorrect_updates


# Path to the input file
input_path = "input.txt"  # Replace with your file path

# Parse the input data
order_rules, updates = parse(input_path)

# Calculate the sum of middle pages for incorrectly ordered updates after correction
result, incorrect_updates = calculate_middle_page_sum(order_rules, updates)

print("Sum of middle page numbers for corrected updates:", result)
print("Corrected updates:", incorrect_updates)
