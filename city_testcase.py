import unittest
from city import get_city_country_name


class CityCountryNameTestCase(unittest.TestCase):

    def test_city_country_name(self):
        city_name = get_city_country_name('Guangzhoua', 'China')
        print('cit name is '+city_name)
        self.assertEqual(city_name, 'Guangzhou In China')


if __name__ == '__main__':
    unittest.main()
