import unittest
from utils import get_word_frequency, split_words

class TestSplitWords(unittest.TestCase):
    def test_split_words(self):
        book = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness..."
        expected_words = ['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of', 'foolishness']
        self.assertEqual(split_words(book), expected_words)
        
        book = "To be or not to be, that is the question."
        expected_words = ['to', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question']
        self.assertEqual(split_words(book), expected_words)
        
        book = "All happy families are alike; each unhappy family is unhappy in its own way."
        expected_words = ['all', 'happy', 'families', 'are', 'alike', 'each', 'unhappy', 'family', 'is', 'unhappy', 'in', 'its', 'own', 'way']
        self.assertEqual(split_words(book), expected_words)
        
class TestGetWordFrequency(unittest.TestCase):
    
    def test_get_word_frequency(self):
        words = ["this", "is", "a", "sample", "sentence", "this", "sentence", "has", "some", "repeated", "words", "like", "this", "and", "sentence"]
        freq_dict = get_word_frequency(words)
        expected = {'this': 3, 'sentence': 3, 'is': 1, 'a': 1, 'sample': 1, 'has': 1, 'some': 1, 'repeated': 1, 'words': 1, 'like': 1, 'and': 1}
        self.assertDictEqual(freq_dict, expected)


if __name__ == '__main__':
    unittest.main()
