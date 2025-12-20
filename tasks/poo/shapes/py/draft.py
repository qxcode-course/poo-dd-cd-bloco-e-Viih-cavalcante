from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, area: int, perimeter: int, name: str):
        self._area: int
        self._perimeter: int
        self._name: str
    def getArea(self) -> int:
        return self._area
    def getPerimeter(self) -> int:
        return self._perimenter
    def getName(self) -> str:
        return self._name
class Point2d(Shape):
    def _init_(self, x: int, y: int):
     super()._init_()
     self.__x: int = x
     self.__y: int = y
    def constructor(self, x: int, y: int):
        return self._x and self._y
    def _str_(self) -> str:
        return f"({self._x}, {self._y})"
class Circle(Shape):
    def _init_(self, name: str, center: Point2d, radius: int):
        super()._init_("Circ")
        self._name: str = " "
        self._center: Point2d
        self._radius: int = 0
    def getName(self):
        return self.__name == "Circ"
    def getArea(self, area: float):
        area == 3,14 *= (self._radius * self._radius)
        return area
    def getPerimeter(self, value: float):
        value == 2 *3,14 * self.__radius
        return value
    def _str_(self) -> str:
        return f"Circ: C=({self._x},{self._y}), R = {self._radius}"
class Retangle(Shape):
    def _init_(self):
        