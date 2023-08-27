class Node:
    def __init__(self, p=0, e=0, nxt=None):
        if nxt is None:
            nxt = dict()
        self.p = p  # pass
        self.e = e  # end
        self.nxt = nxt  # next


class Trie:

    def __init__(self):
        self.root = Node()

    def string_insert(self, word):
        if not word:
            return
        curr = self.root
        curr.p += 1  # root的pass += 1
        for letter in word:
            if curr.nxt.get(letter) is None:
                curr.nxt[letter] = Node()
            curr = curr.nxt[letter]
            curr.p += 1  # letter的pass += 1
        curr.e += 1  # letter的end += 1

    def delete(self, word):
        if self.search(word):
            curr = self.root
            curr.p -= 1
            for letter in word:
                if curr.nxt[letter].p == 1:
                    curr.nxt[letter] = None
                    return
                curr = curr.nxt[letter]
                curr.p -= 1
            curr.e -= 1

    def search(self, word):
        if not word:
            return 0
        curr = self.root
        for letter in word:
            if curr.nxt.get(letter) is None:
                return 0
            curr = curr.nxt[letter]
        return curr.e

    def prefix_num(self, pre_str):
        if not pre_str:
            return 0
        curr = self.root
        for letter in pre_str:
            if curr.nxt.get(letter) is None:
                return 0
            curr = curr.nxt[letter]
        return curr.p


if __name__ == "__main__":
    pass
