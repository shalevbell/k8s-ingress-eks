from app import *
import unittest


class TestWeather(unittest.TestCase):
    def testadress(self):
        self.assertEqual(location_to_dict("mexico")["c_location"], "México")


if __name__ == "__main__":
    unittest.main()