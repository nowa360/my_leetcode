"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {None: None}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr_dict = self.tree

        for char in word:
            if char not in curr_dict:
                curr_dict[char] = {}
            curr_dict = curr_dict[char]

        curr_dict[None] = None

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr_dict = self.tree

        for char in word:
            if char not in curr_dict:
                return False
            curr_dict = curr_dict[char]

        return None in curr_dict

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr_dict = self.tree

        for char in prefix:
            if char not in curr_dict:
                return False
            curr_dict = curr_dict[char]
        return True

