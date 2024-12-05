def is_safe(vals):
    """Check if a sequence of levels is safe."""
    asc = True
    desc = True
    for i in range(1, len(vals)):
        diff = vals[i] - vals[i - 1]
        if diff == 0 or abs(diff) > 3:
            return False
        if diff > 0:
            desc = False
        elif diff < 0:
            asc = False
    return asc or desc

def can_be_safe_with_removal(vals):
    """Check if a sequence of levels can become safe by removing one level."""
    for i in range(len(vals)):
        new_vals = vals[:i] + vals[i + 1:]  # Remove the i-th level
        if is_safe(new_vals):
            return True
    return False

import time

# Start the timer
start_time = time.time()

# Open the file and process each line
safe_reports = 0
safe_vals = []

with open('inputtest.txt', 'r') as fichier:
    for ligne in fichier:
        valeurs = list(map(int, ligne.strip().split()))
        if is_safe(valeurs) or can_be_safe_with_removal(valeurs):
            safe_reports += 1
            safe_vals.append(valeurs)

# End the timer
end_time = time.time()

# Print the results
print("Number of safe reports:", safe_reports)
# Uncomment the following line to see the list of safe values
# print("Safe values:", safe_vals)

# Print the execution time
print("Execution time: {:.2f} seconds".format(end_time - start_time))
