grade = input("Donnez le grade de l'employé : ")
nbr_heures = float(input("Donnez nombre d'heure qu'a travaillé l'employé : "))

if(grade == "A"):
  print(f"salaire = (200*{nbr_heures}) + (1000*{nbr_heures/20})= {200*nbr_heures + 1000*(nbr_heures/20)}")
elif(grade == "B"):
  print(f"salaire = (150*{nbr_heures}) + (800*{nbr_heures/20})= {150*nbr_heures + 1000*(nbr_heures/20)}")
elif(grade == "C"):
  print(f"salaire = (120*{nbr_heures}) + (500*{nbr_heures/15})= {120*nbr_heures + 500*(nbr_heures/15)}")
elif(grade == "D"):
  print(f"salaire = (100*{nbr_heures}) + (350*{nbr_heures/15})= {100*nbr_heures + 350*(nbr_heures/15)}")
elif(grade == "E"):
  print(f"salaire = (80*{nbr_heures}) + (100*{nbr_heures/10})= {80*nbr_heures + 100*(nbr_heures/10)}")
else:
  print("Error , choisi le grade entre A et E")