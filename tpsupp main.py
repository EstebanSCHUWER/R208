import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distanceCoord(self, a, b):
        return math.sqrt((a - self.x)**2 + (b - self.y)**2)

    def distancePoint(self, camarade):
        return math.sqrt((camarade.x - self.x)**2 + (camarade.y - self.y)**2)

def test():
    point1 = Point()
    point2 = Point(3, 4)
    point3 = Point(6, 8)

    print("Coordonnées du point 1:", point1.x, ",", point1.y)
    print("Coordonnées du point 2:", point2.x, ",", point2.y)
    print("Coordonnées du point 3:", point3.x, ",", point3.y)

    distance1 = point1.distanceCoord(3, 4)
    distance2 = point2.distancePoint(point3)

    print("Distance entre le point 1 et (3,4):", distance1)
    print("Distance entre le point 2 et le point 3:", distance2)

if __name__ == "__main__":
    test()
