""" Unit test for the translator module """
import unittest
import translator

#from translator import englishToFrench, double

class TestenglishToFrenchpyth(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.englishToFrench('Goodbye'), 'Au revoir')
        self.assertEqual(translator.englishToFrench('Good evening'), 'Bonsoir')
        self.assertNotEqual(translator.englishToFrench('Goodbye'), 'Goodbye')
        self.assertNotEqual(translator.englishToFrench('Good evening'), 'Good evening')
        self.assertEqual(translator.englishToFrench(0), '0')
        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour')

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.frenchToEnglish('Au revoir'), 'Goodbye')
        self.assertEqual(translator.frenchToEnglish('Bonsoir'), 'Good evening')
        self.assertNotEqual(translator.frenchToEnglish('Au revoir'), 'Au revoir')
        self.assertNotEqual(translator.frenchToEnglish('Bonsoir'), 'Bonsoir')
        self.assertEqual(translator.frenchToEnglish(0), '0')
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello')

unittest.main()
