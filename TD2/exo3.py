import random 

nbr = random.randint(1,100)

essaie = 0 ; 
while(essaie < 7 ):
    essaie = essaie + 1 
    n = int(input("Veuillez sasir un nombre entre 1 et 100 : "))
    if n > nbr :
        print("oups, Veuillez entrer un nombre plus petit")

    elif n < nbr:
        print("oups, Veuillez entrer un nombre plus grand")
    elif n > 100 or n < 1:
        print("oups, Veuillez entrer un nombre entre 1 et 100")
    elif n == nbr :
        print(f"Bravo, vous avez entrer le correct nombre. votre nombre d'essaie est : {essaie}")
        break




