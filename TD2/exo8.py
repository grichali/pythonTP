L=[1,2,5,8,6,2,5,9,1,8,8]

nbr = int(input('Veuillez saisir le nombre : '))
occ = []
for i in range (len(L)):
    if L[i] == nbr :
        occ.append(i)
        
nbr_occ = len(occ)
print(f"{nbr} existe dans la liste {nbr_occ} fois , voici les indice : {occ}")