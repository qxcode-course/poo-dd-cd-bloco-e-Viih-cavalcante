from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def getArea(self) -> float:
        pass

    @abstractmethod
    def getPerimeter(self) -> float:
        pass

    @abstractmethod
    def getName(self) -> str:
        pass

class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x:.2f}, {self.y:.2f})"

class Circle(Shape):
    def __init__(self, center: Point2D, radius: float):
        self._name = "Circ"
        self._center = center
        self._radius = radius

    def getName(self) -> str:
        return self._name

    def getArea(self) -> float:
        return math.pi * self._radius ** 2

    def getPerimeter(self) -> float:
        return 2 * math.pi * self._radius

    def __str__(self) -> str:
        return f"Circ: C={self._center}, R={self._radius:.2f}"

class Rectangle(Shape):
    def __init__(self, p1: Point2D, p2: Point2D):
        self._name = "Rect"
        self._p1 = p1
        self._p2 = p2

    def getName(self) -> str:
        return self._name

    def getArea(self) -> float:
        largura = abs(self._p1.x - self._p2.x)
        altura = abs(self._p1.y - self._p2.y)
        return largura * altura

    def getPerimeter(self) -> float:
        largura = abs(self._p1.x - self._p2.x)
        altura = abs(self._p1.y - self._p2.y)
        return 2 * (largura + altura)

    def __str__(self) -> str:
        return f"Rect: P1={self._p1} P2={self._p2}"
def main():
    shapes = []

    while True:
        entrada = input().strip()

        if entrada == "$end":
            break

        partes = entrada.split()

        if partes[0] == "$circle":
            x = float(partes[1])
            y = float(partes[2])
            r = float(partes[3])
            
            centro = Point2D(x, y)
            circulo = Circle(centro, r)
            shapes.append(circulo)
        for shape in shapes:
            print(shape)
            print(f"Area = {shape.getArea():.2f}")
            print(f"Perimeter = {shape.getPerimeter():.2f}")

if __name__ == "__main__":
    main()
            
