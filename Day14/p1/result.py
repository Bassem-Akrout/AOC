# Let's parse the file "input.txt" and extract the data in a structured format.

# Define the path to the file
file_path = 'input.txt'
def parse(file_path):
    # Parse the file
    parsed_data = []
    with open(file_path, 'r') as file:
        for line in file:
            point_part, velocity_part = line.strip().split(" v=")
            point = list(map(int, point_part.split("=")[1].split(",")))
            velocity = tuple(map(int, velocity_part.split(",")))
            parsed_data.append({"pos": point, "velocity": velocity})
    return parsed_data
print(parse(file_path))

def update(data):

    for i in range(1,7571):
        for bot in data:
            position=bot["pos"]
            speed=bot["velocity"]
            position[0]=(position[0]+speed[0] )% 101
            position[1]=(position[1]+speed[1] )% 103
data=parse(file_path)
update(data)

print(data)
def determine_quadrant(data):
    mid_x=50
    mid_y=51
    s1,s2,s3,s4=0,0,0,0
    for bot in data:
        x, y = bot["pos"][0],bot["pos"][1]
        if x < mid_x and y > mid_y:
            s1 += 1
        elif x > mid_x and y > mid_y:
            s2 += 1
        elif x < mid_x and y < mid_y:
            s3 += 1
        elif x > mid_x and y < mid_y:
            s4 += 1
    return s1*s2*s3*s4
print(determine_quadrant(data))
