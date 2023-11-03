L =  [1,-30,0,-2,500,4,2,100]

M = []

for num in L:
    if num < 0 :
        M.append(num)

for num in L:
    if num >= 0 :
        M.append(num)

print(M)