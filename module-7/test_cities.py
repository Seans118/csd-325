import unittest

import city_functions

# testing city_functions.py
class TestCityFunctions(unittest.TestCase):
    def test_city_country(self):
        results = city_functions.print_city('santiago', 'chile')
        self.assertEqual(results, 'Santiago, Chile')
        
if __name__ == '__main__':
    unittest.main() 
