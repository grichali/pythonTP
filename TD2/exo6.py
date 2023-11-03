L = [1,2,3,4,5,6,7,8,9]

print(L)

num = int(input('Veuillez saisir le nombre a suprimer'))

while num in L :
    L.remove(num)
    
print(f'Voici la liste apres suprimer {num} : {L}')