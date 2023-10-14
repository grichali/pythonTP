
login = input("Entrez votre login : ")
mot_de_passe = input("Entrez votre mot de passe : ")


if login == "admin" and mot_de_passe == "admin":
    print("Bienvenue ! Vous êtes connecté en tant qu'administrateur.")
else:
    print("Login ou mot de passe incorrect. Veuillez réessayer.")
