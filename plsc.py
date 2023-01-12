def plusLongueSc(chaine1,chaine2):
    a=len(chaine1)
    b=len(chaine2)
    if a*b ==0:
        return "" 
    elif chaine1[a-1]==chaine2[b-1]:
        return plusLongueSc(chaine1[:a-1],chaine2[:b-1]) + chaine1[a-1] 
    else:
        c1=plusLongueSc(chaine1,chaine2[:b-1])
        c2=plusLongueSc(chaine1[:a-1],chaine2)
        if len(c1)>len(c2):
            return c1
        else:
            return c2

def present(m):
    for i in range (0,len(m)):
        print("Sequence", i+1, ":", m[i])
    print("Plus Longue Sous Sequence commune:")

def affichePLS(*n):
    tab=[]
    for values in n:
        tab.append(values)
    p=tab[0]
    for i in range(1,len(tab)):
        p=plusLongueSc(p, tab[i]) 
    present(tab)
    return p 
print(affichePLS("abdaadadcbda","baddcadacabd","3urHGDaAAdBfb2Khg", "saahnfbgb789"))


