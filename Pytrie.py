

class Trie(object):

    def __init__(self, *args):
        self._trie = {}
        for word in args:
            tmp = self._trie
            if isinstance(word, str):
                for letter in word:
                    tmp = tmp.setdefault(letter, {})
            else:
                raise TypeError("Trie only support string type.")


if __name__ == '__main__':
    trie = Trie('abc', 'abd', 'xyz')
    print(trie._trie)