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
    return matrix,mv




def move(dir,init,matrix):
    x,y=init
    dx,dy= dir
    while matrix[x][y] not in ["#","."]:
        x+=dx
        y+=dy
    if matrix[x][y] =="#":
        #fail
        return init
    else :
        x0,y0=init
        matrix[x][y]='O'
        matrix[x0+dx][y0+dy],matrix[x0][y0]=matrix[x0][y0],"."
        return (x0+dx,y0+dy)
def sum(matrix):
    sum=0
    for i,row in enumerate(matrix):
        for j,elt in enumerate(row):
            if elt=="O":
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
        elif mv=="v":
            dir=(1,0)
        elif mv=="^":
            dir=(-1,0)
            
        else:
            
            dir=(0,1)
        init=move(dir,init,matrix)
    print(sum(matrix))
if __name__ == "__main__":
    main()