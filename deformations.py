
from readmdict import MDX

# https://github.com/ffreemt/readmdict

def get_full_dict(dict_fn: str) -> List[str]:
    if not dict_fn.endswith(".mdx"):
        raise Exception("dict file should be end with .mdx")
    
    items = [*MDX(dict_fn).items()]
    all_dict_word = []
    for key, _ in items:
        key_value = key.decode('utf-8')
        if " " not in key_value:
            all_dict_word.append(key_value)
    return all_dict_word


if __name__ == '__main__':
    print(mdx['a big fish in a little pond'])
