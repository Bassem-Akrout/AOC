def asc_desc(vals):
    asc = True
    desc = True
    prec = vals[0]
    for elt in vals[1:]:
        if elt == prec:
            return False, False
        elif elt < prec:
            asc = False
            if prec - elt > 3:
                return False, False
        else:
            desc = False
            if elt - prec > 3:
                return False, False
        prec = elt
    return asc, desc

def stable_asc_desc(vals):
    asc = True
    desc = True
    prec = vals[0]
    new_res=asc_desc(vals[1:])
    if True in new_res:
        return new_res
    
    for idx in range(1,len(vals)):
        elt=vals[idx]
        if elt == prec:
            print("eq")
            new_res=asc_desc(vals[:idx] + vals[idx+1:])
            print("return eq",new_res)
            return new_res
        elif elt < prec:
            print("dsc")
            if asc:
                new_res=asc_desc(vals[:idx] + vals[idx+1:])
                if new_res==(False,False):
                    new_res=asc_desc(vals[:idx-1] + vals[idx:]) #[29, 28, 27, 25, 26, 25, 22, 20]
                if new_res==(False,False):
                    asc= False
                else:
                    print("return dsc",new_res)
                    return new_res
            if prec - elt > 3:
                new_res=asc_desc(vals[:idx] + vals[idx+1:])
                print("return dsc 2",new_res)
                return new_res
        else:
            print("asc")
            if desc:
                new_res=asc_desc(vals[:idx] + vals[idx+1:])
                if new_res==(False,False):
                    new_res=asc_desc(vals[:idx-1] + vals[idx:]) #[29, 28, 27, 25, 26, 25, 22, 20]
                if new_res==(False,False):
                    desc= False
                else:
                    print("return asc",new_res)
                    return new_res
            if elt - prec > 3:
                new_res=asc_desc(vals[:idx] + vals[idx+1:])
                print("return asc2",new_res)
                return new_res
        if int(asc or desc)==0:
            return False,False
        prec = elt
    print("return END",asc, desc)
    return asc, desc

def main():
    # Ouvrir le fichier et lire les lignes
    with open('input.txt', 'r') as fichier:
        res = 0
        cnt=0
        safe_vals=[]

        # Lire et ajouter chaque valeur dans le heap correspondant
        for ligne in fichier:
            cnt+=1
            valeurs = list(map(int, ligne.strip().split()))  # Conversion explicite en int
            asc, desc = stable_asc_desc(valeurs)
            res += int(asc or desc)
            if asc or desc:
                safe_vals.append(valeurs)
        print(res)
        print(cnt)
        print(safe_vals)

print([29, 28, 27, 25, 26, 25, 22, 20])
print(stable_asc_desc([29, 28, 27, 25, 26, 25, 22, 20]))
if __name__=='__main__':
    main()
    