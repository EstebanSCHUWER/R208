class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, *args):
        if len(args) == 0:
            self.bas_gauche = Point()
            self.haut_droit = Point(1, 1)
            self.longueur = 1
            self.hauteur = 1
        elif len(args) == 2:
            if isinstance(args[0], Point) and isinstance(args[1], Point):
                self.bas_gauche = args[0]
                self.haut_droit = args[1]
                self.longueur = abs(args[1].x - args[0].x)
                self.hauteur = abs(args[1].y - args[0].y)
            else:
                self.bas_gauche = Point()
                self.haut_droit = Point(args[0], args[1])
                self.longueur = args[0]
                self.hauteur = args[1]


def surface(self):
        return self.longueur * self.hauteur

    def perimetre(self):
        return 2 * (self.longueur + self.hauteur)

    def bas_gauche(self):
        return self.bas_gauche

    def haut_gauche(self):
        return Point(self.bas_gauche.x, self.haut_droit.y)

    def bas_droit(self):
        return Point(self.haut_droit.x, self.bas_gauche.y)

    def haut_droit(self):
        return self.haut_droit

    def point_dans_rectangle(self, point):
        return self.bas_gauche.x <= point.x <= self.haut_droit.x and self.bas_gauche.y <= point.y <= self.haut_droit.y

def main():
    point1 = Point()
    point2 = Point(2, 3)

    rectangle1 = Rectangle()
    rectangle2 = Rectangle(3, 4)
    rectangle3 = Rectangle(point1, point2)

    print("Surface du rectangle 1:", rectangle1.surface())
    print("Périmètre du rectangle 1:", rectangle1.perimetre())
    print("Coin bas gauche du rectangle 1:", rectangle1.bas_gauche.x, ",", rectangle1.bas_gauche.y)
    print("Coin haut gauche du rectangle 1:", rectangle1.haut_gauche().x, ",", rectangle1.haut_gauche().y)
    print("Coin bas droit du rectangle 1:", rectangle1.bas_droit().x, ",", rectangle1.bas_droit().y)
    print("Coin haut droit du rectangle 1:", rectangle1.haut_droit.x, ",", rectangle1.haut_droit.y)
    print("Le point1 est dans le rectangle 1:", rectangle1.point_dans_rectangle(point1))
    print("Le point2 est dans le rectangle 1:", rectangle1.point_dans_rectangle(point2))

    print("Surface du rectangle 2:", rectangle2.surface())
    print("Périmètre du rectangle 2:", rectangle2.perimetre())

    print("Surface du rectangle 3:", rectangle3.surface())
    print("Périmètre du rectangle 3:", rectangle3.perimetre())

if __name__ == "__main__":
    main()
