def is_x_mas_fixed(grid, row, col):
    # Check if the X centered at (row, col) matches the fixed pattern
    n = len(grid)
    m = len(grid[0])

    # Ensure the pattern fits within bounds
    if row - 1 < 0 or row + 1 >= n or col - 1 < 0 or col + 1 >= m:
        return False

    # Extract the required positions
    top_left = grid[row - 1][col - 1]
    bottom_right = grid[row + 1][col + 1]
    top_right = grid[row - 1][col + 1]
    bottom_left = grid[row + 1][col - 1]
    center = grid[row][col]

    return (
        center == "A" and
        (
            (top_left == "S" and bottom_right == "M" and top_right == "M" and bottom_left == "S") or
            (top_left == "M" and bottom_right == "S" and top_right == "S" and bottom_left == "M") or
            (top_left == "S" and bottom_right == "M" and top_right == "S" and bottom_left == "M") or
            (top_left == "M" and bottom_right == "S" and top_right == "M" and bottom_left == "S")
        )
    )

def count_x_mas_fixed(grid):
    n = len(grid)
    m = len(grid[0])
    count = 0

    # Iterate over all possible centers
    for row in range(n):
        for col in range(m):
            if is_x_mas_fixed(grid, row, col):
                count += 1

    return count

def main():
    # Read the input file and store lines in memory
    with open('input.txt', 'r') as file:
        grid = [line.strip() for line in file]

    # Count X-MAS patterns
    total_x_mas = count_x_mas_fixed(grid)

    print(f"Total X-MAS patterns found: {total_x_mas}")

if __name__ == "__main__":
    main()
