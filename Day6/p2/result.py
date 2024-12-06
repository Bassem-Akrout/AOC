import time  # Importing the time module

def main():
    start_time = time.time()  # Start the timer

    # Read the input file and store lines in memory
    parsed_grid, guard_position = parse_grid_and_find_guard("input.txt")
    counter = 0
    direction = [-1, 0]  # Initial direction (up)
    directions_matrix = [[None for _ in range(len(parsed_grid[0]))] for _ in range(len(parsed_grid))]
    directions_matrix[guard_position[0]][guard_position[1]] = direction

    # Test each possible position for placing an obstacle
    for i in range(len(parsed_grid)):
        for j in range(len(parsed_grid[0])):
            if parsed_grid[i][j] in ['#', '^']:  # Skip positions that are obstacles or the guard's start
                continue

            # Create a new grid with the obstacle added
            new_grid = add_obs(parsed_grid, (i, j))
            # Reset variables for testing
            stuck = 2
            test_direction = direction[:]
            test_guard_position = guard_position[:]
            directions_matrix_copy = [row[:] for row in directions_matrix]

            # Simulate the guard's movement with the new obstacle
            while stuck == 2:
                stuck, test_direction, test_guard_position = is_stuck(
                    new_grid, test_guard_position, test_direction, directions_matrix_copy
                )

            if stuck == 1:  # Guard gets stuck in a loop
                counter += 1

    end_time = time.time()  # End the timer
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"Counter: {counter}")
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")  # Print the time in seconds with 2 decimal precision
    return counter



def parse_grid_and_find_guard(file_path):
    guard_position = None
    parsed_grid = []
    with open(file_path, 'r') as file:
        for row_idx, line in enumerate(file):
            line = line.strip()  # Remove any trailing whitespace/newlines
            parsed_grid.append(list(line))  # Convert the line into a list of characters
            if '^' in line and guard_position is None:
                guard_position = (row_idx, line.index('^'))  # Record the position of '^'
    return parsed_grid, guard_position


def add_obs(grid, position):
    """Add an obstacle at the specified position."""
    new_grid = [row[:] for row in grid]
    new_grid[position[0]][position[1]] = '#'
    return new_grid


def is_stuck(parsed_grid, guard_position, direction, directions_matrix):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # Up, Right, Down, Left
    while True:
        # Compute the next position
        next_pos = (guard_position[0] + direction[0], guard_position[1] + direction[1])

        # Check if next position is out of bounds
        if (next_pos[0] < 0 or next_pos[0] >= len(parsed_grid) or
                next_pos[1] < 0 or next_pos[1] >= len(parsed_grid[0])):
            return 0, None, None  # Guard leaves the grid

        # Check if next position is an obstacle
        if parsed_grid[next_pos[0]][next_pos[1]] == '#':
            # Turn right (update direction)
            current_dir_idx = directions.index(direction)
            direction = directions[(current_dir_idx + 1) % 4]
            return 2, direction, guard_position

        # Check if the guard is revisiting the same position with the same direction
        if directions_matrix[next_pos[0]][next_pos[1]] == direction:
            return 1, None, None  # Guard is stuck in a loop

        # Mark the position as visited with the current direction
        directions_matrix[next_pos[0]][next_pos[1]] = direction

        # Update the guard's position
        guard_position = next_pos
        return 2, direction, guard_position


if __name__ == "__main__":
    main()
