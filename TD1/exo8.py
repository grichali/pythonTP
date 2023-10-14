somme_produits = 0
somme_coefficients = 0

for i in range(1, 5):
    note = float(input(f"Note {i} : "))
    coef = int(input("Coefficient : "))
    

    somme_produits += note * coef
    somme_coefficients += coef

moyenne = somme_produits / somme_coefficients

print(f"Moyenne de ces 4 notes : {moyenne:.2f}")

if moyenne >= 10:
    print("Semestre validé")
else:
    print("Semestre non validé")

