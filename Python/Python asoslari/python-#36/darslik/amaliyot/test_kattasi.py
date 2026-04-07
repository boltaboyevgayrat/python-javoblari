import unittest
from funksiyalar import kattasi

class KattasiTest(unittest.TestCase):
    def test_kattasi(self):
        formatted_son = kattasi(2, 3, 1)
        self.assertEqual(formatted_son, 3)

unittest.main()

