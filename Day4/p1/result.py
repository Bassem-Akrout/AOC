import re

def generate_diagonals(grid):
    diagonals = []
    num_lines = len(grid)
    num_cols = len(grid[0])

    # Left-to-right diagonals
    for start_col in range(num_cols):
        diagonal = ""
        row, col = 0, start_col
        while row < num_lines and col < num_cols:
            diagonal += grid[row][col]
            row += 1
            col += 1
        diagonals.append(diagonal)

    for start_row in range(1, num_lines):
        diagonal = ""
        row, col = start_row, 0
        while row < num_lines and col < num_cols:
            diagonal += grid[row][col]
            row += 1
            col += 1
        diagonals.append(diagonal)

    # Right-to-left diagonals
    for start_col in range(num_cols - 1, -1, -1):
        diagonal = ""
        row, col = 0, start_col
        while row < num_lines and col >= 0:
            diagonal += grid[row][col]
            row += 1
            col -= 1
        diagonals.append(diagonal)

    for start_row in range(1, num_lines):
        diagonal = ""
        row, col = start_row, num_cols - 1
        while row < num_lines and col >= 0:
            diagonal += grid[row][col]
            row += 1
            col -= 1
        diagonals.append(diagonal)

    return diagonals

def explore_str(pattern, text):
    # Count overlapping matches using a sliding window
    count = 0
    start = 0
    print("looking for pattern: ",pattern," in text: " ,text)
    while True:
        match = re.search(pattern, text[start:])
        if not match:
            break
        count += 1
        start += match.start() + 1  # Start one position after the current match
    return count

def main():
    # Read the input file and store lines in memory
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file]

    print("Input lines:")
    for line in lines:
        print(line)
    print("\n")

    # Generate all diagonals
    diagonals = generate_diagonals(lines)

    print("Generated diagonals:")
    for diagonal in diagonals:
        print(diagonal)
    print("\n")

    # Patterns to search for
    patterns = [r"XMAS", r"SAMX"]  # Including reversed word

    # Count matches in rows, columns, and diagonals
    total_count = 0

    # Check rows
    print("Checking rows...")
    for line in lines:
        print("row :",line)
        for pattern in patterns:
            count = explore_str(pattern, line)
            if count > 0:
                print(f"Pattern '{pattern}' found {count} times in row: {line}")
            total_count += count

    # Check columns
    print("Checking columns...")
    for col in range(len(lines[0])):
        column = ''.join(row[col] for row in lines)
        for pattern in patterns:
            count = explore_str(pattern, column)
            if count > 0:
                print(f"Pattern '{pattern}' found {count} times in column: {column}")
            total_count += count

    # Check diagonals
    print("Checking diagonals...")
    for diagonal in diagonals:
        for pattern in patterns:
            count = explore_str(pattern, diagonal)
            if count > 0:
                print(f"Pattern '{pattern}' found {count} times in diagonal: {diagonal}")
            total_count += count

    print("\nTotal count of 'XMAS':", total_count)

if __name__ == "__main__":
    main()
