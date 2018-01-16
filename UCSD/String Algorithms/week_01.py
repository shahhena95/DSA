import sys


class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

#needs improvement to store pattern and search text in it
class Trie:
    """
    Trie to store text and searches text in it
    """
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def char_to_index(self, ch):
        return ord(ch)-ord('A')

    def insert(self, key):
        parent = self.root
        length = len(key)
        for level in range(length):
            index = self.char_to_index(key[level])
            if not parent.children[index]:
                parent.children[index] = self.get_node()
            parent = parent.children[index]

        parent.isEndOfWord = True

    def search(self, key):
        parent = self.root
        length = len(key)
        for level in range(length):
            index = self.char_to_index(key[level])
            if not parent.children[index]:
                return False
            parent = parent.children[index]

        return parent != None and parent.isEndOfWord


def main():
    trie = Trie()
    user_input = sys.stdin.readlines()
    user_input = [line.strip('\n') for line in user_input]
    for word in user_input:
        trie.insert(word)

    print(trie.search(user_input[0]))

if __name__ == "__main__":
    main()
