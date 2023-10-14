total_facture = 0

for i in range(1, 3):  
    print(f"\nArticle {i}:")
    nom_article = input("Nom de l'article : ")
    prix_article = float(input("Prix unitaire : "))
    quantite_article = int(input("Quantité : "))


    montant_ht = prix_article * quantite_article
    montant_ttc = montant_ht + (montant_ht * 0.2)


    print(f"Montant total de l'article {i} : {montant_ttc:.2f} €")


    total_facture += montant_ttc


print(f"\nMontant total de la facture : {total_facture:.2f} €")
