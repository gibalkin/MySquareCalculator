from abc import ABC, abstractmethod
import math

"""
Класс фигур
"""


class Figure(ABC):
    @abstractmethod
    def SquareFigure(self):
        pass


"""
Треугольник
"""

class Triangle(Figure):
    def __init__(self, sideA, sideB, sideC):
        """
        Стороны треугольника
        """
        for side in (sideA, sideB, sideC):
            if not isinstance(side, (int, float)):
                raise TypeError("Стороны треугольника должны быть числами")
            if side <= 0:
                raise ValueError("Стороны треугольника должны быть положительными числами")

        self.sideA = float(sideA)
        self.sideB = float(sideB)
        self.sideC = float(sideC)

        if self.sideA + self.sideB <= self.sideC or self.sideA + self.sideC <= self.sideB or self.sideB + self.sideC <= self.sideA:
            raise ValueError("Сумма любых двух сторон треугольника должна быть больше третьей стороны")

    def SquareFigure(self):
        """
        Площадь треугольника
        """
        sperimeter = (self.sideA + self.sideB + self.sideC) / 2
        return math.sqrt(sperimeter * (sperimeter - self.sideA) * (sperimeter - self.sideB) * (sperimeter - self.sideC))

    def Rectangular(self):
        """
        Является ли треугольник прямоугольным
        """
        sides = sorted([self.sideA, self.sideB, self.sideC])
        return math.isclose(sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2)


"""
Окружность
"""

class Circle(Figure):
    def __init__(self, radius):
        """Радиус"""
        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус должен быть числом")
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")

        self.radius = float(radius)

    def SquareFigure(self):
        """
        Площадь круга
        """
        return math.pi * self.radius ** 2


"""
Произвольный четырехугольник
"""

class Quadrilateral(Figure):
    def __init__(self, diagonal_1, diagonal_2, angle_in_degrees):
        """
        Диагонали и угол между ними
        """
        for value in (diagonal_1, diagonal_2, angle_in_degrees):
            if not isinstance(value, (int, float)):
                raise TypeError("Диагонали и угол должны быть числами")

        if diagonal_1 <= 0 or diagonal_2 <= 0:
            raise ValueError("Диагонали должны быть положительными числами")
        if not (0 < angle_in_degrees < 180):
            raise ValueError("Угол должен быть между 0 и 180 градусами")

        self.diagonal_1 = float(diagonal_1)
        self.diagonal_2 = float(diagonal_2)
        self.angle_in_degrees = float(angle_in_degrees)

    def SquareFigure(self):
        """
        Площадь произвольного четырехугольника
        """
        return 0.5 * self.diagonal_1 * self.diagonal_2 * math.sin(math.radians(self.angle_in_degrees))


"""
Многоугольник по координатам
"""

class Figure_by_coordinates(Figure):
    def __init__(self, vertices):
        if not isinstance(vertices, list) or not all(
                isinstance(vertex, tuple) and len(vertex) == 2 for vertex in vertices):
            raise TypeError("Координаты должны быть списком кортежей с двумя числами")
        if len(vertices) < 3:
            raise ValueError("Многоугольник должен иметь как минимум 3 вершины")

        self.vertices = vertices

    def SquareFigure(self):
        """
        Вычисление площади многоугольника по координатам вершин, используя формулу Гаусса.
        """
        n = len(self.vertices)
        area = 0
        for i in range(n):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % n]
            area += x1 * y2 - y1 * x2

        return abs(area) / 2
