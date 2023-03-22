from pdfminer.high_level import extract_text
from utils import split_words, get_word_frequency

dict_file_name = "resources/weishi_v3/weishi_eng_cn_dict.mdx"

if __name__ == "__main__":
    print("word parser")
    # read book, and extrac the txt from pdf
    book_txt = extract_text("Functional-Programming-in-Scala.pdf")
    # get all the words of the book
    book_words = split_words(book_txt)
    # get word frequency of the book
    book_word_freq = get_word_frequency(book_words)
