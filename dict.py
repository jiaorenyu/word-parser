import re
from settings import *
from readmdict import MDX

# https://github.com/ffreemt/readmdict

from typing import List

def get_full_dict_words(dict_fn: str) -> List[str]:
    if not dict_fn.endswith(".mdx"):
        raise Exception("dict file should be end with .mdx")
    
    items = [*MDX(dict_fn).items()]
    all_dict_word = []
    for key, _ in items:
        key_value = key.decode('utf-8')
        if " " not in key_value:
            all_dict_word.append(key_value)
    return all_dict_word


def get_full_dict(dict_fn: str) -> dict:
    if not dict_fn.endswith(".mdx"):
        raise Exception("dict file should be end with .mdx")
    
    mdx = {}
    items = [*MDX(dict_fn).items()]

    for key, value in items:
        key = key.decode('utf-8')
        value = value.decode('utf-8')
        if " " not in key:
            mdx[key] = value

    return mdx

def get_formation_map(fn):
    fp = open(fn, "r")
    _formation_map = dict()
    for dict_line in fp.readlines():
        arr = [x.strip() for x in dict_line.split(" ")]
        if len(arr) == 2:
            if 'secrets' in arr:
                print("in in in !")
                print(arr)
            (formation, _origin) = arr
            _formation_map[formation] = _origin

    return _formation_map


def load_etymology_mdx(etymology_mdx: str):
    items = [*MDX(etymology_mdx).items()]
    mdx = {}
    for key, val in items:
        mdx[str(key.decode('utf-8'))] = val.decode('utf-8')

    return mdx

def load_etymology(etymology_fn: str):
    etymology_dict = {}
    with open(etymology_fn) as fp:
        for line in fp:
            word_ety = line.strip().split()
            if len(word_ety) == 2:
                word = word_ety[0]
                ety = word_ety[1]
                etymology_dict[word] = ety

    return etymology_dict

def save_full_etymology(etymology_mdx: str):
    etymology = load_etymology_mdx(etymology_mdx)
    def find_ety_for_word(etymology, the_word, recursive=2):
        recursive -= 1
        if isinstance(the_word, int):
            return 'notfound'
        if the_word in etymology:
            e_text = etymology[the_word]
            if 'Old English' in e_text or 'German' in e_text:
                return 'anglo'
            elif 'French' in e_text:
                return 'french'
            elif 'Latin' in e_text:
                return 'latin'
            else:
                if recursive < 0:
                    return 'else'
                else:
                    got = re.search(r'entry://(\w+)', e_text)
                    # print("got", got)
                    if got:
                        return find_ety_for_word(got.group(1), recursive)
                    else:
                        return 'else'
        else:
            return 'notfound'
        
    with open(f"resources/etymology.txt", "w") as fp:
        for word in etymology:
            ety = find_ety_for_word(etymology, word)
            fp.write(f"{word} {ety}\n")

def save_etymology(word_ety_dict: dict, book_name: str):
    with open(f"resources/etymology/{book_name}/"+ety, "w") as fp:
        for word, ety in word_ety_dict.items():
            fp.write(f"{word} {ety}\n")


if __name__ == "__main__":
    # get all the dict words
    full_dict_words = get_full_dict_words(dict_mdx_path)
    with open(full_dict_words_path, "w") as fp:
        fp.write("\n".join(full_dict_words))

    
    save_full_etymology(etymology_mdx_path)