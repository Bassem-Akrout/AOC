def parse_input_to_matrix(input_file):
    res=[]
    with open(input_file, 'r') as file:
        for line in file:
            l=[]
            for elt in line:
                if elt.isdigit():
                    l.append(int(elt))
                else:
                    if elt!="\n":
                        l.append(-1)
            res.append(l)

    return res
directions=[(-1,0),(1,0),(0,1),(0,-1)]
def heads(matrix):
    pos=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                pos.append((i,j))
    return pos
def nines_for_head(matrix,pos):
    positions=set()
    positions.add(pos)
    for i in range(1,10):
        new_positions=set()
        for pos in positions:
            neighnours=[]
            for dir in directions:
                if 0<=pos[0]+dir[0]<len(matrix)and 0<=pos[1]+dir[1]<len(matrix[0]):
                    neighnours.append((pos[0]+dir[0],pos[1]+dir[1]))
            for neighbour in neighnours:
                if matrix[neighbour[0]][neighbour[1]]==i:
                    new_positions.add(neighbour)
        positions=new_positions
    return positions
def trail_for_head(matrix, pos):
    trails = set()
    trails.add((pos,))  # Utiliser un tuple au lieu d'une liste
    for i in range(1, 10):
        new_trails = set()
        for trail in trails:
            neighbours = []
            current_pos = trail[-1]
            for dir in directions:
                if 0 <= current_pos[0] + dir[0] < len(matrix) and 0 <= current_pos[1] + dir[1] < len(matrix[0]):
                    neighbours.append((current_pos[0] + dir[0], current_pos[1] + dir[1]))
            for neighbour in neighbours:
                if matrix[neighbour[0]][neighbour[1]] == i:
                    new_trail = trail + (neighbour,)  # Ajouter au tuple
                    new_trails.add(new_trail)
        trails = new_trails
    return trails


matrix=parse_input_to_matrix("input.txt")
print("matrix",matrix)
headss=heads(matrix)
print("headss",headss)
print("trail_for_head(headss[0])",trail_for_head(matrix,headss[0]))


def main():
    matrix=parse_input_to_matrix("input.txt")
    headss=heads(matrix)
    sum=0
    for head in headss:
        sum+=len(trail_for_head(matrix,head))
    print(sum)
main()
