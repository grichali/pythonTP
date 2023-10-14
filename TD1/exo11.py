pois = float(input("POIS :"))
taille = float(input("TAILLE :"))

imc = pois/(taille*taille)

if(imc>=40):
  print("obésité morbide ou massive")
elif(imc>=35 and imc < 40):
  print("obésité sévère")
elif(imc>=30 and imc < 35):
  print("obésité sévère")
elif(imc>=25 and imc < 30):
  print("Surpoids")
elif(imc>=18.5 and imc < 25):
  print("corpulence normale")
elif(imc>=16.5 and imc < 18.5):
  print("Maigreur")
else:
  print("Famine")