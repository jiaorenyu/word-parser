from settings import full_dict_words_fn, book_word_freq_path
from pdfminer.high_level import extract_text
from utils import split_words, get_word_frequency
import sys, os
from pathlib import Path


def get_dict_words():
    dict_words = set()
    with open(full_dict_words_fn) as fp:
        for word in fp:
            dict_words.add(word.strip())

    return dict_words

def write_word_freq(book_word_freq: dict):
    book_word_freq_file_path = book_word_freq_path.format(book_name=book_fn)
    Path(os.path.dirname(book_word_freq_file_path)).mkdir(parents=True, exist_ok=True)

    with open(book_word_freq_file_path, "w") as fp:
        word_freq_list = []
        for word, freq in book_word_freq.items():
            word_freq_list.append(word + "," + str(freq))
        
        fp.write("\n".join(word_freq_list))


if __name__ == "__main__":
    print("word parser")
    book_fn = sys.argv[1]

    dict_words = get_dict_words()

    # read book, and extrac the txt from pdf
    print("start extract text from book")
    book_txt = extract_text(book_fn)
    print("finish extract text from book")
    # get all the words of the book
    print("start split word")
    all_book_words = split_words(book_txt)
    print("finish split words")
    # get word frequency of the book
    print("start get the word freq from words")
    book_word_freq = get_word_frequency(all_book_words)
    
    write_word_freq(book_word_freq)
    print("finish get the word freq from words")

    

