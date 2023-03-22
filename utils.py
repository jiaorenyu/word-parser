import string
from collections import Counter
import re

def split_words(book):
    # Remove punctuation from the book
    book = book.translate(str.maketrans('', '', string.punctuation))
    
    # Split the book into words
    words = book.split()
    
    # Convert all words to lowercase
    words = [word.lower() for word in words]
    
    return words


def get_word_frequency(words):
    """
    Returns a dictionary of word frequencies given a list of words.
    """
    freq_dict = dict(Counter(words))
    return dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))
