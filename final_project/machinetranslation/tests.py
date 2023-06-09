import unittest

from translator import english_to_french, french_to_english

class TestEntoFr(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("hello"), "bonjour")
        self.assertEqual(english_to_french("good"), "bien")
        self.assertNotEqual(english_to_french("hello"), "hi")
    
class TestFrtoEn(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("bien"), "good")
        self.assertNotEqual(french_to_english("bonjour"), "salut")

unittest.main()