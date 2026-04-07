import unittest
from funksiyalar import katta_harf

class KattaHarfTest(unittest.TestCase):
    def test_katta_harf(self):
        self.assertEqual(katta_harf(['olma', 'nok', 'banan']), ['Olma', 'Nok', 'Banan'])
        
unittest.main()