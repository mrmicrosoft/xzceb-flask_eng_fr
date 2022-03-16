import unittest
from translator import englishToFrench, frenchToEnglish

class TestModules(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertNotEqual(englishToFrench("Hello"), "")

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertNotEqual(frenchToEnglish("Bonjour"), "")

if __name__ == "__main__":
    unittest.main()

