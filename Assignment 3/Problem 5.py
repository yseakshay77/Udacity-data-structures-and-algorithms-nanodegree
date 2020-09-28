class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}
        # print (self.children)
    def insert(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()
        else:
            pass

    def suffixes(self, suffix=''):
        results = []

        if self.is_word and suffix != '':
            results.append(suffix)

        if len(self.children) == 0:
            return results

        results = []

        if self.is_word and suffix != '':
            results.append(suffix)

        for char in self.children:
            results.extend(self.children[char].suffixes(suffix=suffix+char))

        # print (results)
        return results


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            node.insert(char)
            node = node.children[char]

        node.is_word = True

    def find(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        # print (node.children)


        return node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

print ("\n Starting from t : ")
result = MyTrie.find('t')
result_2 = result.suffixes()
for x in result_2:
    print (x)
# print (result_2)

print ("\n Starting from a : ")
result = MyTrie.find('a')
result_2 = result.suffixes()
for x in result_2:
    print (x)