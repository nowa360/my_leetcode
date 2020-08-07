class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.'
        to represent any one letter.
        :type word: str
        :rtype: bool
        """

        stack = [(self.root, word)]
        while stack:
            node, curr_word = stack.pop()

            if not curr_word:
                if node.is_word:
                    return True
            elif curr_word[0] == '.':
                for t_node in node.children.values():
                    stack.append((t_node, curr_word[1:]))
            else:
                if curr_word[0] in node.children:
                    node = node.children[curr_word[0]]
                    stack.append((node, curr_word[1:]))
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
