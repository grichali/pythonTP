L1= [1,3,6,78,35,88,55] 
L2= [12,24,35,24,88,120,155] 
L3=[]

for nbr in L1:
    if nbr in L2:
        L3.append(nbr)
        
print(L3)
