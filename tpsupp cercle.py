import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

class Cercle:
    def __init__(self, rayon, centre=Point()):
        self.centre = centre
        self.rayon = rayon

    def diametre(self):
        return self.rayon * 2

    def perimetre(self):
        return 2 * math.pi * self.rayon

    def surface(self):
        return math.pi * (self.rayon ** 2)

    def intersection(self, autre_cercle):
        distance_centres = math.sqrt((autre_cercle.centre.x - self.centre.x)**2 + (autre_cercle.centre.y - self.centre.y)**2)
        return distance_centres < self.rayon + autre_cercle.rayon

    def point_dans_cercle(self, point):
        distance_centre_point = math.sqrt((point.x - self.centre.x)**2 + (point.y - self.centre.y)**2)
        return distance_centre_point <= self.rayon

def main():
    point1 = Point()
    point2 = Point(3, 4)

    cercle1 = Cercle(5)
    cercle2 = Cercle(3, point2)

    print("Rayon du cercle 1:", cercle1.rayon)
    print("Centre du cercle 1:", cercle1.centre.x, ",", cercle1.centre.y)
    print("Diamètre du cercle 1:", cercle1.diametre())
    print("Périmètre du cercle 1:", cercle1.perimetre())
    print("Surface du cercle 1:", cercle1.surface())

    print("Rayon du cercle 2:", cercle2.rayon)
    print("Centre du cercle 2:", cercle2.centre.x, ",", cercle2.centre.y)
    print("Diamètre du cercle 2:", cercle2.diametre())
    print("Périmètre du cercle 2:", cercle2.perimetre())
    print("Surface du cercle 2:", cercle2.surface())

    print("Les cercles sont en intersection:", cercle1.intersection(cercle2))

    print("Le point1 est dans le cercle 1:", cercle1.point_dans_cercle(point1))
    print("Le point2 est dans le cercle 1:", cercle1.point_dans_cercle(point2))

if __name__ == "__main__":
    main()
