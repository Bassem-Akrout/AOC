def parse_input_to_matrix(input_file):
    positions = {}
    lines = []  # To store all lines for length calculations
    with open(input_file, 'r') as file:
        for numline, line in enumerate(file):
            stripped_line = line.strip()  # Stripping newlines and spaces
            lines.append(stripped_line)  # Append to lines for later length checks
            for idx, letter in enumerate(stripped_line):
                if letter.isdigit() or letter.isalpha():  # Check if letter is a digit or letter
                    if letter not in positions:
                        positions[letter] = [(numline, idx)]
                    else:
                        positions[letter].append((numline, idx))
    # Number of rows and max columns
    num_rows = len(lines)
    num_cols = max(len(line) for line in lines) if lines else 0  # Max length of lines

    print(positions)
    return positions, num_rows, num_cols

# Test the function
#positions, num_rows, num_cols = parse_input_to_matrix("input.txt")
#print(f"Number of rows: {num_rows}, Number of columns: {num_cols}")

# Test the function with the input file
parse_input_to_matrix("input.txt")
def main():
    positions, num_rows, num_cols = parse_input_to_matrix("input.txt")
    counter = 0
    visited=set()
    for elt in positions.keys():
        values = positions[elt]
        for idx, pos in enumerate(values):
            for idx2 in range(idx + 1, len(values)):  # Commence à idx + 1
                pos2 = values[idx2]
                new1 = ( pos[0],  pos[1])
                new2 = (pos2[0] ,  pos2[1] )
                diff1 = ( pos[0] - pos2[0], pos[1] - pos2[1])
                diff2 = ( pos2[0] - pos[0], pos2[1] - pos[1])
                print(pos, pos2)
                while 0 <= new1[0] < num_rows and 0 <= new1[1] < num_cols:
                    if new1 not in visited:
                        counter += 1
                        visited.add(new1)
                        print(pos, pos2,new1)
                    new1=(new1[0]+diff1[0],new1[1]+diff1[1])

                while 0 <= new2[0] < num_rows and 0 <= new2[1] < num_cols:
                    if new2 not in visited:
                        counter += 1
                        visited.add(new2)
                    new2=(new2[0]+diff2[0],new2[1]+diff2[1])
    
    print(counter)
    print(len(visited))
    return counter

main()