import unittest

from plants import COLOMBIAN_PLANTS
from plants import get_random_plant


class TestPlants(unittest.TestCase):

    def test_successfully_get_random_plant(self):
        random_plant = get_random_plant()
        self.assertEqual(type(random_plant), str)
        self.assertTrue(random_plant in COLOMBIAN_PLANTS)

if __name__ == '__main__':
    unittest.main()
