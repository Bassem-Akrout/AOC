def asc_desc(values):
    """
    Determines if the sequence of values is strictly ascending or strictly descending,
    with adjacent differences of at least 1 and at most 3, and no equal adjacent elements.
    Returns a tuple (is_ascending, is_descending) indicating the sequence type.
    """
    is_ascending = True
    is_descending = True
    previous_value = values[0]

    for current_value in values[1:]:
        if current_value == previous_value:
            # Adjacent values must not be equal
            return False, False
        elif current_value < previous_value:
            # Sequence is not strictly ascending
            is_ascending = False
            if previous_value - current_value > 3:
                # Difference is too large for descending sequence
                return False, False
        else:
            # Sequence is not strictly descending
            is_descending = False
            if current_value - previous_value > 3:
                # Difference is too large for ascending sequence
                return False, False
        previous_value = current_value

    return is_ascending, is_descending


def stable_asc_desc(values):
    """
    Determines if the sequence can be made strictly ascending or descending
    by removing at most one element (Problem Dampener).
    Returns a tuple (is_ascending, is_descending) indicating the sequence type.
    """
    is_ascending = True
    is_descending = True
    previous_value = values[0]

    # First, check if removing the first element makes the sequence valid
    result = asc_desc(values[1:])
    if True in result:
        return result

    for index in range(1, len(values)):
        current_value = values[index]

        if current_value == previous_value:
            # Equal adjacent values detected
            # Try removing the current element
            modified_values = values[:index] + values[index + 1:]
            result = asc_desc(modified_values)
            return result

        elif current_value < previous_value:
            # Descending step detected
            if is_ascending:
                # Try removing the current or previous element to fix ascending sequence
                modified_values = values[:index] + values[index + 1:]
                result = asc_desc(modified_values)
                if result == (False, False):
                    # Try removing the previous element for edge case like [29, 28, 27, 25, 26, 25, 22, 20]
                    modified_values = values[:index - 1] + values[index:]
                    result = asc_desc(modified_values)
                if result == (False, False):
                    is_ascending = False
                else:
                    return result
            if previous_value - current_value > 3:
                # Difference too large, try removing the current element
                modified_values = values[:index] + values[index + 1:]
                result = asc_desc(modified_values)
                return result

        else:
            # Ascending step detected
            if is_descending:
                # Try removing the current or previous element to fix descending sequence
                modified_values = values[:index] + values[index + 1:]
                result = asc_desc(modified_values)
                if result == (False, False):
                    # Try removing the previous element for edge case like [29, 28, 27, 25, 26, 25, 22, 20]
                    modified_values = values[:index - 1] + values[index:]
                    result = asc_desc(modified_values)
                if result == (False, False):
                    is_descending = False
                else:
                    return result
            if current_value - previous_value > 3:
                # Difference too large, try removing the current element
                modified_values = values[:index] + values[index + 1:]
                result = asc_desc(modified_values)
                return result

        # If the sequence is neither ascending nor descending, it's unsafe
        if not (is_ascending or is_descending):
            return False, False

        previous_value = current_value

    return is_ascending, is_descending


import time

def main():
    """
    Reads the input file 'input.txt' and processes each line as a report.
    Counts and prints the number of safe reports according to the specified rules.
    Measures and prints the execution time of the program.
    """
    start_time = time.time()  # Start the timer

    # Open the file and read the lines
    with open('inputtest.txt', 'r') as file:
        safe_reports_count = 0  # Number of safe reports
        safe_values = []        # List to store safe reports

        # Process each line (report) in the file
        for line in file:
            values = list(map(int, line.strip().split()))
            is_ascending, is_descending = stable_asc_desc(values)
            # Increment the count if the report is safe
            if is_ascending or is_descending:
                safe_reports_count += 1
                safe_values.append(values)

    end_time = time.time()  # End the timer

    # Print the number of safe reports
    print("Number of safe reports:", safe_reports_count)

    # Uncomment the following line to see the list of safe reports
    # print("Safe reports:", safe_values)

    # Print the execution time
    print("Execution time: {:.2f} seconds".format(end_time - start_time))


# Uncomment the following lines to run the program
# if __name__ == '__main__':
#     main()


# Uncomment the following lines to test the function with a specific sequence
# test_sequence = [29, 28, 27, 25, 26, 25, 22, 20]
# print("Test sequence:", test_sequence)
# print("Result:", stable_asc_desc(test_sequence))

# Uncomment the following line to run the main function
if __name__ == '__main__':
    main()
