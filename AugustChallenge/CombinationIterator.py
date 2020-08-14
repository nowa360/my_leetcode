import collections

"""
August 13 Challenge - Iterator for Combination

Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number 
combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
 

Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.

"""


class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.que = collections.deque()
        self.comb_helper(characters, 0, "", combinationLength)

    def comb_helper(self, word, start, curr, length):
        if length == 0:
            self.que.appendleft(curr)
            return
        for i in xrange(start, len(word)):
            self.comb_helper(word, i + 1, curr + word[i], length - 1)

    def next(self):
        """
        :rtype: str
        """
        return self.que.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.que:
            return True
        return False

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
