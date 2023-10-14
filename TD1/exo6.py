
num1 = float(input("Veuillez saisir le premier nombre : "))
num2 = float(input("Veuillez saisir le deuxième nombre : "))


if (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
    print("Le produit des deux nombres est positif.")
elif num1 == 0 or num2 == 0:
    print("Le produit des deux nombres est nul.")
else:
    print("Le produit des deux nombres est négatif.")
