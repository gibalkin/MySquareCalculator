import unittest
from math import pi, sin, radians
from square import Triangle, Circle, Quadrilateral, Figure_by_coordinates

class TestFigures(unittest.TestCase):

    #Тест треугольника
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.SquareFigure(), 6.0, places=2)

    def test_triangle_is_rectangular(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.Rectangular())

        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.Rectangular())

    def test_triangle_invalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(3, 3, 6)

        with self.assertRaises(ValueError):
            Triangle(3, 3, 7)

        with self.assertRaises(ValueError):
            Triangle(-1, 4, 5)

        with self.assertRaises(TypeError):
            Triangle("6fuyhk", 4, 5)

    #Тест окружности
    def test_circle_area(self):
        circle = Circle(1)
        self.assertAlmostEqual(circle.SquareFigure(), pi, places=2)

        circle = Circle(2)
        self.assertAlmostEqual(circle.SquareFigure(), 4*pi, places=2)

        circle = Circle(1.27833)
        self.assertAlmostEqual(circle.SquareFigure(), (1.27833**2)*pi, places=2)

    def test_circle_invalid_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)

        with self.assertRaises(TypeError):
            Circle("erghh2")

    #Тест четырехугольника
    def test_quadrilateral_area(self):
        quadrilateral = Quadrilateral(5, 6, 90)
        self.assertAlmostEqual(quadrilateral.SquareFigure(), 15.0, places=2)

        quadrilateral = Quadrilateral(5, 6, 30)
        self.assertAlmostEqual(quadrilateral.SquareFigure(), 5 * 6 * sin(radians(30)) / 2, places=2)

    def test_quadrilateral_invalid_values(self):
        with self.assertRaises(ValueError):
            Quadrilateral(-5, 6, 90)

        with self.assertRaises(ValueError):
            Quadrilateral(5, 6, 190)

        with self.assertRaises(TypeError):
            Quadrilateral("wefgre", 6, 90)

    #Тест многоугольника
    def test_polygon_area(self):
        # Треугольник
        vertices = [(0, 0), (4, 0), (4, 3)]
        polygon = Figure_by_coordinates(vertices)
        self.assertAlmostEqual(polygon.SquareFigure(), 6.0, places=2)

        # Четырехугольник
        vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
        polygon = Figure_by_coordinates(vertices)
        self.assertAlmostEqual(polygon.SquareFigure(), 12.0, places=2)

        # Многоугольник
        vertices = [(-5.747, 75), (-25.1, 0), (-3.3, 7.95), (0, 8.24), (54.3333, 25.2), (4.4949, 0), (32, -7.9)]
        polygon = Figure_by_coordinates(vertices)
        self.assertAlmostEqual(polygon.SquareFigure(), 1706.94, places=2)

    def test_polygon_invalid_vertices(self):
        with self.assertRaises(ValueError):
            Figure_by_coordinates([(0, 0), (4, 0)])

        with self.assertRaises(TypeError):
            Figure_by_coordinates("invalid vertices")

        with self.assertRaises(TypeError):
            Figure_by_coordinates([(0, 0), (4, 0), "invalid vertex"])
