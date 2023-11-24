class Point:
    
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def getX(slef):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self,x):
        self.x = x
        
    def setY(self,y):
        self.y = y
        
    def __str__():
        return f'Point : ({self.x},{self.y})'
    
    
class Rectangle(Point):
    
    def __init__(self , x, y ,longeur , largeur):
        super().__init__(x,y)
        self.longeur = longeur 
        self.largeur = largeur
        
    def getLargeur(self):
        return self.largeur
    
    def getLongeur(self):
        return self.longeur
    
    def setLargeur(self, largeur):
        self.largeur = largeur
        
    def setLongeur(self, longeur):
        self.longeur = longeur
        
    def __str__():
        return f'Rectangle de langeur ({self.largeur}) , longeur ({self.longeur}) '
    
class Parallelepipede(Rectangle):

    def __init__(self, x, y, longeur, largeur, hauteur):
        super().__init__(x, y, longeur, largeur)
        self.hauteur = hauteur

    def getHauteur(self):
        return self._hauteur

    
    def setHauteur(self, hauteur):
        self._hauteur = hauteur

    def aire(self):
        
        return 2 * (self.longeur * self.largeur + self.longeur * self.hauteur + self.largeur * self.hauteur)

    def volume(self):
        
        return self.longeur * self.largeur * self.hauteur

    def __str__(self):
        return f"Parallelepipede de langeur ({self.longeur}), largeur ({self.largeur}), hauteur ({self.hauteur})"



parall = Parallelepipede(1, 2, 3, 4, 5)

aire = parall.aire()
print(aire)

print(parall.volume())

# Afficher le parallélépipède
print(parall)
