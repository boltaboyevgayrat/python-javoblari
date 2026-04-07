import unittest
from funksiyalar import juft_son

class JuftSonTest(unittest.TestCase):
    def test_juft(self):
        self.assertEqual(juft_son(list(range(10))), list(range(0, 10, 2)))

unittest.main()