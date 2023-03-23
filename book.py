from settings import full_dict_words_fn, book_word_freq_path
from pdfminer.high_level import extract_text
from utils import split_words, get_word_frequency
import sys, os
from pathlib import Path

dict_file_name = "resources/weishi_v3/weishi_eng_cn_dict.mdx"

if __name__ == "__main__":
    print("word parser")
    book_fn = sys.argv[1]
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
    print("finish get the word freq from words")
    

    book_word_freq_file_path = book_word_freq_path.format(book_name=book_fn)
    Path(os.path.dirname(book_word_freq_file_path)).mkdir(parents=True, exist_ok=True)

    with open(book_word_freq_file_path, "w") as fp:
        word_freq_list = []
        for word, freq in book_word_freq.items():
            word_freq_list.append(word + "," + str(freq))
        
        fp.write("\n".join(word_freq_list))


    

