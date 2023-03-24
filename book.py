from dict import get_formation_map, load_etymology
from settings import word_freq_path, word_etymology_path, full_dict_words_path, formation_path, etymology_path
from pdfminer.high_level import extract_text
from utils import save_dict, split_words, get_word_frequency
import sys, os
from pathlib import Path
from wordfreq import zipf_frequency
from typing import List
from pathlib import Path


def get_dict_words():
    dict_words = set()
    with open(full_dict_words_path) as fp:
        for word in fp:
            dict_words.add(word.strip())

    return dict_words

def mapping_to_origin(formation: dict, book_word_freq: dict):
    origin_book_word_freq = {}
    for word, freq in book_word_freq.items():
        origin = formation[word] if word in formation else word
        origin_book_word_freq[origin] = book_word_freq[origin] if origin in book_word_freq else freq
    return origin_book_word_freq


def filter_book_words(word_freq: dict, min_freq: int = 1, max_freq: int = 3.5):
    filtered_word_freq = {}
    for word, freq in word_freq.items():
        fq = zipf_frequency(word, 'en')
        if min_freq <= fq <= max_freq:
            filtered_word_freq[word] = freq

    return filtered_word_freq


def find_word_etymology(word_list: List[str], etymology: dict):
    word_etymoloty = {}
    for word in word_list:
        word_etymoloty[word] = etymology[word] if word in etymology else "notfound"
    return word_etymoloty

if __name__ == "__main__":
    print("word parser")
    book_fn = sys.argv[1]

    # Main steps:
    # 1. Read book, and get all the book word frequency: f(book) -> W1
    # 2. Get the formation map: load(formation_file) -> F1
    # 3. Get the etymology map: load(etymology_file) -> E1
    # 4. Mapping the book word to the origin by F1 if it exists: f(F1, W1) -> W2
    # 5. Filter W2 to get the word need to learn, depends on
    #       [min_freq, max_freq]
    #    `freq = zipf_frequency(word, 'en')` in wordfreq
    #    Filter by min_freq < freq < max_freq
    #    f(W2, min_freq, max_freq) -> W3
    # 6. Get the etymology of the book word W3: f(E1, W3) -> E2


    # Step1
    print("Step1 start")
    dict_words = get_dict_words()
    book_txt = extract_text(book_fn)
    all_book_words = split_words(book_txt)
    book_word_freq = get_word_frequency(all_book_words)
    print("Step1 end")

    # Step2
    print("Step2 start")
    formation_map = get_formation_map(formation_path)
    print("Step2 end")

    # Step3
    print("Step3 start")
    etymology = load_etymology(etymology_path)
    print("Step3 end")

    # Step4
    print("Step4 start")
    origin_book_word_freq = mapping_to_origin(formation_map, book_word_freq)
    print("Step4 end")

    # Step5
    print("Step5 start")
    filtered_word_freq = filter_book_words(origin_book_word_freq)
    print("Step5 end")

    # Step6
    print("Step6 start")
    word_etymology = find_word_etymology(filtered_word_freq.keys(), etymology)
    print("Step6 end")
    
    # Save result
    print("start saving data")
    book_name = os.path.basename(book_fn).split(".")[0]
    word_freq_path = word_freq_path.format(book_name=book_name)
    word_etymology_path = word_etymology_path.format(book_name=book_name)
    Path(os.path.dirname(word_freq_path)).mkdir(parents=True, exist_ok=True)
    Path(os.path.dirname(word_etymology_path)).mkdir(parents=True, exist_ok=True)

    save_dict(filtered_word_freq, word_freq_path)
    save_dict(word_etymology, word_etymology_path)
    print("end saving data")


