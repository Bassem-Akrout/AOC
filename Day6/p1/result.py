def main():
    # Read the input file and store lines in memory
    parsed_grid, guard_position = parse_grid_and_find_guard("input.txt")
    counter = 0
    direction = [-1, 0]  # Initial direction (up)
    out = False
    while not out:
        counter_tmp, out, direction, guard_position = get_out(parsed_grid, guard_position, direction)
        counter += counter_tmp
    print(counter)
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


def get_out(parsed_grid, guard_position, direction):
    counter = 0
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # Up, Right, Down, Left
    while True:
        # Compute the next position
        next_pos = (guard_position[0] + direction[0], guard_position[1] + direction[1])
        
        # Check if next position is out of bounds
        if (next_pos[0] < 0 or next_pos[0] >= len(parsed_grid) or
                next_pos[1] < 0 or next_pos[1] >= len(parsed_grid[0])):
            return counter, True, direction, guard_position
        
        # Check if next position is an obstacle (#)
        if parsed_grid[next_pos[0]][next_pos[1]] == '#':
            # Turn right (update direction)
            current_dir_idx = directions.index(direction)
            direction = directions[(current_dir_idx + 1) % 4]
            return counter, False, direction, guard_position
        
        # If next position is not visited, mark it and increase counter
        if parsed_grid[next_pos[0]][next_pos[1]] != 'X':
            parsed_grid[next_pos[0]][next_pos[1]] = 'X'
            counter += 1
        
        # Update the guard's position
        guard_position = next_pos


if __name__ == "__main__":
    main()
