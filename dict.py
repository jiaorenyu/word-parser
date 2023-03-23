from deformations import get_full_dict_words
from settings import *

if __name__ == "__main__":
    full_dict_words = get_full_dict_words(dict_file_name)
    with open(full_dict_words_fn, "w") as fp:
        fp.write("\n".join(full_dict_words))
