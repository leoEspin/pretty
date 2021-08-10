import unittest
from prettifier import pretty

class testito(unittest.TestCase):
    def test_base_case(self):
        self.assertTrue(pretty(1000000) == '1M')
        self.assertTrue(pretty(2500000.34) == '2.5M')
        self.assertTrue(pretty(532) == '532')
        self.assertTrue(pretty(1123456789) == '1.1B')
        self.assertTrue(pretty(9487634567534) == '9.5T')

if __name__ == '__main__':
    unittest.main()