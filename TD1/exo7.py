nb1 = int(input("Veuillez sasir le numero 1 : "))
nb2 = int(input("Veuillez sasir le numero 2 : "))
op = input("Veuillez sasir l'operation")
match op :
    case'*':
        print(str(nb1),op,str(nb2),"= ", str(nb2*nb1))
    case'+':
        print(str(nb1),op,str(nb2),"= ", str(nb2+nb1))
    case'-':
        print(str(nb1),op,str(nb2),"= ", str(nb2-nb1))
    case'/':
        print(str(nb1),op,str(nb2),"= ", str(nb2/nb1))