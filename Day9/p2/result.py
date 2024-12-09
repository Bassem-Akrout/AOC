def parse_input_to_matrix(input_file):
    res=[]
    with open(input_file, 'r') as file:
        for line in file:
            res=line.strip()
    print(res)
    return res


# Test the function with the input file

def transform(line):
    list_free=[]
    list_not_free=[]
    for idx,elt in enumerate(line):
        if idx%2==0:
            list_not_free.append([str((idx//2))]*int(elt))
        else:
            list_free.append(["."]*int(elt))
    liste=[]
    for i in range(min(len(list_not_free), len(list_free))):
        if list_not_free[i] !=[]:
            liste.append(list_not_free[i])
        if list_free[i] !=[]:
            liste.append(list_free[i])
    # Add the remaining elements from the longer list
    if len(list_not_free) > len(list_free):
        liste.append(list_not_free[-1])
    elif len(list_free) > len(list_not_free):
        liste.append(list_free[-1])

    print(liste)
    return liste
        
def transform3(list_not_free,not_free):
    new_list=[]
    print("list_not_free",list_not_free)
    start=0
    for elt in list_not_free:
        #print(elt)
        length=len(elt)
        new_list.append(not_free[start:start+length])
        start+=length
    print("new_list",new_list)
    return new_list

def transform2(list):
    print(list)
    right=len(list)-1
    while right >0:
        #print(right)
        if list[right][0]==".":
            right-=1
        else:
            left=0
            while left<right:
                #print(left,right)
                if not(list[left][0]=="." and len(list[left])>=len(list[right])):
                    left+=1
                else:
                    if len(list[left])==len(list[right]):
                        list[left],list[right]=list[right],list[left]
                        
                    else:
                        len1=len(list[left])
                        len2=len(list[right])
                        list[left]=list[right]
                        list[right]=len2*["."]
                        list.insert(left+1,["."]*(len1-len2))
                        right+=1
                    break
            right-=1
            #print(list)
    new=[]
    for elt in list:
        new.extend(elt)
    return new

def checksum(liste):
    s=0
    print(liste)
    for idx,elt in enumerate(liste):
        if elt==".":
            #print(s)
            continue
            return s
        else:
            #print("elt",elt)
            s+=idx*int(elt)
    print(s)
    return s
liste=transform(parse_input_to_matrix("input.txt"))
my_list = liste

# File path (adjust as needed)
file_path = 'output.txt'

# Write list to file
with open(file_path, 'w') as file:
    for item in my_list:
        file.write(f"{item}\n")  # Each item is written on a new line

print(f"List has been written to {file_path}.")

liste2=transform2(liste)
print(liste2)
my_list = liste2

# File path (adjust as needed)
file_path = 'output2.txt'

# Write list to file
with open(file_path, 'w') as file:
    for item in my_list:
        file.write(f"{item}\n")  # Each item is written on a new line

print(f"List has been written to {file_path}.")
#
checksum(liste2)

    
