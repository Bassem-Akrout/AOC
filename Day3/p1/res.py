import re
def main():

    sum=0
    with open('input.txt', 'r') as file:
        for line in file:
            sum+=explore_str(line)
    print(sum)


def explore_str(corrupted_memory):
    # Regular expression pattern to match valid mul(X,Y)
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"


    # Extract all valid matches
    matches = re.findall(pattern, corrupted_memory)

    # Calculate the sum of all valid multiplications
    total_sum = sum(int(x) * int(y) for x, y in matches)
    return total_sum

if __name__=="__main__":
    main()