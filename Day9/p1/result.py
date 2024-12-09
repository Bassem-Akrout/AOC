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
    for i in range(len(list_free)):
        liste.extend(list_not_free[i]+list_free[i])
    liste.extend(list_not_free[-1])
    print(list_not_free)
    print(list_free)
    print(liste)
    copy=liste.copy()
    copy.sort(reverse=True)
    print(copy)
    last_digit_index = max(i for i, x in enumerate(copy) if x.isdigit())
    print(liste[:last_digit_index])
    dot_count = liste[:last_digit_index].count('.')
    print(dot_count)
    return list_not_free,list_free,dot_count
        
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

def transform2(list_not_free,list_free,last_permut):
    not_free=[]
    free=[]
    for l in list_not_free:
        not_free.extend(l)
    for l in list_free:
        free.extend(l)
    print("not_free",not_free)
    print("free",free)
    print(len(not_free)-len(free))
    for i in range(len(not_free)):
        #print("not_free",not_free)
        #print("free",free)
        if i>=last_permut:
            break
        else:
            print(not_free[len(not_free)-i-1],free[i])
        not_free[len(not_free)-i-1],free[i]=free[i],not_free[len(not_free)-i-1]
    liste=[]
    print("not_free",not_free)
    print("free",free)
    not_free3=transform3(list_not_free,not_free)
    free3=transform3(list_free,free)
    print("not_free3",not_free3)
    print("free3",free3)
    for i in range(len(free3)):
        liste.extend(not_free3[i]+free3[i])
    print(liste)
    return liste
def checksum(liste):
    s=0
    for idx,elt in enumerate(liste):
        if elt==".":
            print(s)
            return s
        s+=idx*int(elt)
    print(s)
    return s
list_not_free,list_free,dot_count=transform(parse_input_to_matrix("input.txt"))
liste=transform2(list_not_free,list_free,dot_count)

checksum(liste)

    
