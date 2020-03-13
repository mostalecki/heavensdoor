import unittest

from car import Car
from exceptions import IllegalCarError


class CarTestCase(unittest.TestCase):
    def setUp(self):
        self.car = Car(4, 1500, 6)

    def test_total_car_mass(self):
        self.assertEqual(self.car.total_mass, 1780)

    def test_car_mass(self):
        with self.assertRaises(IllegalCarError):
            self.car.car_mass = 2500

    def test_car_pax_count(self):
        with self.assertRaises(IllegalCarError):
            self.car.pax_count = 0

        with self.assertRaises(IllegalCarError):
            self.car.pax_count = 6
