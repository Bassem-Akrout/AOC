def parse_input_to_matrix(input_file):
    matrix=[]
    mv=[]
    with open(input_file, 'r') as file:
        for line in file:
            if line[0] not in [">","^","<","v"]:
                row=[]
                for letter in line.strip():
                    row.append(letter)
                matrix.append(row)
            else:
                mv+=line.strip()
        matrix.pop()
        new_matrix=[]
        for line in matrix:
            new_line=[]
            for elt in line:
                if elt=='.':
                    new_line.append(".")
                    new_line.append(".")
                elif elt=='O':
                    new_line.append("[")
                    new_line.append("]")
                    
                elif elt=='#':
                    new_line.append("#")
                    new_line.append("#")
                else:
                    new_line.append("@")
                    new_line.append(".")
            new_matrix.append(new_line)
    return new_matrix,mv




def move_h(dir,init,matrix):
    x,y=init
    dx,dy= dir
    counter=0

    while matrix[x][y] not in ["#","."]:
        x+=dx
        y+=dy
        counter+=1
    if matrix[x][y] =="#":
        #fail
        return init
    else :
        ndx,ndy=-dx,-dy
        for _ in range(counter):
            matrix[x][y]=matrix[x+ndx][y+ndy]
            x+=ndx
            y+=ndy
        matrix[x][y]="."
        return (x+dx,y+dy)


def try_move(dir,pos,matrix,boxes):
    x,y=pos
    dx,dy= dir
    if matrix[x][y]=='[':
        if (x,y+1) not in boxes:
            boxes.add((x,y+1))
            try_move(dir,(x,y+1),matrix,boxes)
        if (x+dx,y+dy+1) not in boxes:
            boxes.add((x+dx,y+dy+1))
            try_move(dir,(x+dx,y+dy+1),matrix,boxes)
    elif matrix[x][y]==']':
        if (x,y-1) not in boxes:
            boxes.add((x,y-1))
            try_move(dir,(x,y-1),matrix,boxes)
        if (x+dx,y+dy-1) not in boxes:
            boxes.add((x+dx,y+dy-1))
            try_move(dir,(x+dx,y+dy-1),matrix,boxes)
    else:
        boxes.discard(pos)

def move_v1(dir,init,matrix):
    x,y=init
    dx,dy= dir
    if matrix[x+dx][y+dy]=='#':
        return init
    boxes=set()
    try_move(dir,(x+dx,y+dy),matrix,boxes)
    
    for box in boxes:
        xk,yk=box
        if matrix[xk+dx][yk+dy]=='#':
            return init
    if dir==(-1,0):
        sorted_boxes = sorted(boxes, key=lambda x: (x[0], x[1]))
    
    else:
        sorted_boxes = sorted(boxes, key=lambda x: (-x[0], x[1]))
    for box in sorted_boxes:
        x,y=box
        matrix[x][y],matrix[x+dx][y+dy]=matrix[x+dx][y+dy],matrix[x][y]

    x,y=init
    matrix[x][y],matrix[x+dx][y+dy]=matrix[x+dx][y+dy],matrix[x][y]
    return x+dx,y+dy
def sum(matrix):
    sum=0
    for i,row in enumerate(matrix):
        for j,elt in enumerate(row):
            if elt=="[":
                sum+=100*i+j
    return sum
def main():

    matrix,mvs=parse_input_to_matrix("input.txt")
    init=(0,0)
    for i,row in enumerate(matrix):
        for j,elt in enumerate(row):
            if elt=="@":
                init=(i,j)
    for mv in mvs:
        if mv=="<":
            dir=(0,-1)
            init=move_h(dir,init,matrix)
        elif mv=="v":
            dir=(1,0)
            init=move_v1(dir,init,matrix)
        elif mv=="^":
            dir=(-1,0)
            init=move_v1(dir,init,matrix)
        else:
            dir=(0,1)
            init=move_h(dir,init,matrix)
    print(sum(matrix))
if __name__ == "__main__":
    main()
