list=[554735 ,45401, 8434, 0 ,188, 7487525, 77, 7]

for i in range(25):
    print("step : ",i)
    print(len(list))
    newlist=[]
    for nbr in list:
        if nbr==0:
            newlist.append(1)
        elif len(str(nbr))%2==0:
            #print(nbr,str(nbr)[:len(str(nbr))//2])
            newlist.append(int(str(nbr)[:len(str(nbr))//2]))
            newlist.append(int(str(nbr)[len(str(nbr))//2:]))
        else:
            newlist.append(nbr*2024)
    list=newlist
        # Save the new list to a file
    filename = f"output_step_{i}.txt"
    with open(f"{filename}", "w") as file:
        file.write("\n".join(map(str, newlist)))
print(len(list))