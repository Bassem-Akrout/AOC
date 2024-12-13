import re
import numpy as np

def parse_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    machines = []
    pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
    matches = re.findall(pattern, data)

    for match in matches:
        xa, ya, xb, yb, px, py = map(int, match)
        machines.append({
            'M': [[xa,xb ], [ya, yb]],
            'Prize': [px, py]
        })

    return machines

def solve_linear_system(machine):
    M = np.array(machine['M'])
    Prize = np.array(machine['Prize'])

    rank = np.linalg.matrix_rank(M)

    if rank == 0:
        # If rank is 0, the system doesn't depend on inputs; no unique solution
        return None
    elif rank == 1:
        print("rank 1")
        # Find the row with the smallest non-zero values
        non_zero_rows = [row for row in M if any(row)]
        smallest_row = min(non_zero_rows, key=lambda row: min(abs(val) for val in row if val != 0))
        a, b = smallest_row
        x, y = Prize
        if a != 0 and b != 0:
            A = x / a
            B = y / b
            if A.is_integer() and B.is_integer() and A >= 0 and B >= 0:
                return int(A), int(B)
        return None
    else:
        
        # Use np.linalg.solve for a full-rank system
        try:
            solution = np.linalg.solve(M, Prize)
            print(solution)
            rounded_solution = np.round(solution)
            if np.allclose(solution, rounded_solution, atol=1e-9) and all(x >= 0 for x in rounded_solution):
                return tuple(map(int, rounded_solution))
            else:
                return None
        except np.linalg.LinAlgError:
            return None


def solve_all(machines):
    results = []
    for i, machine in enumerate(machines):
        solution = solve_linear_system(machine)
        results.append({
            'Machine': i + 1,
            'Solution': solution
        })
    return results

# Example usage
machines = parse_input('input.txt')
results = solve_all(machines)
sum=0
for result in results:
    print(f"Machine {result['Machine']}:")
    if result['Solution']:
        sum+=3*result['Solution'][0]+result['Solution'][1]
        print("  Solution:", result['Solution'])
    else:
        print("  No solutions found.")
print(sum)
