distance = float(input("Veuillez sasir la distance en km "))
time = float(input("Veuillez sasir le temps en minute "))
distance = distance * 1000
time = time * 60 
v = distance / time 
print("La vitesse est : " + str(v))