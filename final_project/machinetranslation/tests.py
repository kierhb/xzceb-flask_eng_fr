import unittest

from translator import french_to_english

class TestTranslator(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

class TestTranslator(unittest.TestCase):
    def test_french_to_english(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Konnichiwa')

from translator import english_to_french

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertNotEqual(eenglish_to_french('Hello'), 'Konnichiwa')

if __name__=='__main__':
    unittest.main()