
from readmdict import MDX

# https://github.com/ffreemt/readmdict

dict_file_name = "resources/weishi_v3/weishi_eng_cn_dict.mdx"
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


if __name__ == '__main__':
    mdx = get_full_dict(dict_file_name)
    print(mdx['abandon'])
