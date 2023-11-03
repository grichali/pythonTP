def euroToMad(prixeuro):
    prixmad = prixeuro * 10.86 
    return prixmad

def madToEuro(prixmad):
    prixeuro = prixmad * 0.092
    return prixeuro 

valeur = 0
valeurs_converties = []
conversion_direction = input("Choisissez la direction de la conversion (euro_to_mad ou mad_to_euro) : ")

while  valeur >= 0:
    
    valeur = float(input("Veuillez sasire le prix a calculer : (entrer un nombre negatife pour arreter)"))
    
    if conversion_direction == 'euro_to_mad':
        valeurs_converties.append(euroToMad(valeur))
    elif conversion_direction == 'mad_to_euro':
        valeurs_converties.append(madToEuro(valeur))
    else :
        print("Direction de conversion non valide. Choisissez 'euro_to_mad' ou 'mad_to_euro'.")
        break
        
        
        
print(f"Valeurs converties  : {valeurs_converties} ")
