class NumberTransformer:
    def transform_number(self, nbr: int) -> list:
        """Apply the transformation rules to a single integer and return a list of resulting integers."""
        if nbr == 0:
            # Replace 0 with 1
            return [1]
        else:
            nbr_str = str(nbr)
            if len(nbr_str) % 2 == 0:
                # Even length: split into two parts
                midpoint = len(nbr_str) // 2
                first_half = int(nbr_str[:midpoint])
                second_half = int(nbr_str[midpoint:])
                return [first_half, second_half]
            else:
                # Odd length: multiply by 2024
                return [nbr * 2024]

def aggregate_transform(initial_numbers, start_step=1, end_step=3):
    # Build initial counts dictionary from the given list
    counts = {}
    for n in initial_numbers:
        counts[n] = counts.get(n, 0) + 1

    transformer = NumberTransformer()

    for step in range(start_step, end_step + 1):
        print(f"Processing step: {step}")
        new_counts = {}
        for nbr, cnt in counts.items():
            transformed_numbers = transformer.transform_number(nbr)
            for tn in transformed_numbers:
                new_counts[tn] = new_counts.get(tn, 0) + cnt
        counts = new_counts

    # After all steps, print final size
    final_size = sum(counts.values())
    print("Final step size:", final_size)

    # Optionally, to see what numbers we ended up with:
    # for number, count in counts.items():
    #     print(number, ":", count)
    #return counts

if __name__ == "__main__":
    initial_list = [554735, 45401, 8434, 0, 188, 7487525, 77, 7]
    # Example: run 3 steps of transformations
    final_counts = aggregate_transform(initial_list, start_step=1, end_step=75)
