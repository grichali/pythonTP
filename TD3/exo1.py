def delta(a, b, c):
    return b**2 - 4*a*c

def nombre_racines(a, b, c):
    discriminant = delta(a, b, c)

    if discriminant > 0:
        return 2  
    elif discriminant == 0:
        return 1  
    else:
        return 0  


def affiche_nombre_racines(a, b, c):
    nombre = nombre_racines(a, b, c)

    if nombre == 2:
        print("Deux solutions réelles distinctes.")
    elif nombre == 1:
        print("Une solution réelle double.")
    else:
        print("Pas de solution réelle.")


def racine1(a, b, c):
    discriminant = delta(a, b, c)

    if discriminant < 0:
        return None  
    else:
        return (-b + (discriminant**0.5)) / (2*a)

def racine2(a, b, c):
    discriminant = delta(a, b, c)

    if discriminant < 0:
        return None  
    else:
        return (-b - (discriminant**0.5)) / (2*a)


def conversion_temps(h, m, s):
    return h * 3600 + m * 60 + s


def temps_ecoule(heure1, minute1, seconde1, heure2, minute2, seconde2):
    temps1 = conversion_temps(heure1, minute1, seconde1)
    temps2 = conversion_temps(heure2, minute2, seconde2)
    return abs(temps2 - temps1) 


def conversion_distance(km, m, cm):
    return km * 1000 + m + cm / 100


def vitesse(distance_km, distance_m, distance_cm, heure, minute, seconde):
    distance_meters = conversion_distance(distance_km, distance_m, distance_cm)
    temps_en_secondes = conversion_temps(heure, minute, seconde)

    if temps_en_secondes == 0:
        return "La division par zéro n'est pas autorisée."
    else:
        return distance_meters / temps_en_secondes

def somme(m, n):

    if m >= n:
        raise ValueError("m doit être strictement inférieur à n")
    
    result = sum(range(m, n + 1))
    
    return result