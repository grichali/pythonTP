L=[1,2,5,8,6,2,5,9,1,8,8]

el = set()

for i in range(len(L)-1 , -1 , -1):
    if L[i] in el :
        del L[i]
    else :
        el.add(L[i])
        
print(L)