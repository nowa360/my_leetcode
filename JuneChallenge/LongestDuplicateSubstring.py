"""
NOT MY SOLUTION

JUNE 19 CHALLENGE - Longest Duplicate Substring


Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The
occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring,
the answer is "".)



Example 1:

Input: "banana"
Output: "ana"
Example 2:

Input: "abcd"
Output: ""


Note:

2 <= S.length <= 10^5
S consists of lowercase English letters.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.duplicateCount = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.longestDuplicateWord = ''

    def insert(self, word):
        rootNode = self.root
        for i, char in enumerate(word):
            if char not in rootNode.children:
                rootNode.children[char] = TrieNode()
            rootNode = rootNode.children[char]
            substring = word[:i + 1]
            rootNode.duplicateCount += 1
            if rootNode.duplicateCount >= 2:
                if len(substring) > len(self.longestDuplicateWord):
                    self.longestDuplicateWord = substring

        # class Solution(object):
        #     def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str

        Trie
        root
        | | |
        b a n
        | | |      
        a n a
        | |
        n a
        |
        a
        ...
        longestWord = ""

        if already there, 
        field => longestWordAtChar: ''
        """
        #         trie = Trie()
        #         trieRoot = trie.root

        #         # build our trie
        #         for i, char in enumerate(S):
        #             substring = S[i:]
        #             trie.insert(substring)
        #         return trie.longestDuplicateWord

        '''
        Above is Trie Solution but it is too slow
        '''


class Solution:
    def __init__(self):
        pass

    def search(self, leftOfMid, baseConstant, modulus, stringLength, nums):
        """
        Rabin-Karp with polynomial rolling hash.
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.

        Time Complexity: O(NlogN). O(logN) for binary search and O(N) for Rabin-Karp algo

        Space: O(N) to keep the hashset

        * important mistake learnings
            use binary search
        """
        # compute the hash of string S[:L]
        stringHash = 0
        for i in range(leftOfMid):
            stringHash = (stringHash * baseConstant + nums[i]) % modulus

        # already seen hashes of strings of length L
        seen = {stringHash}
        # const value to be used often : a**L % modulus
        baseConstantLeftOfMid = pow(baseConstant, leftOfMid, modulus)
        for start in range(1, stringLength - leftOfMid + 1):
            # compute rolling hash in O(1) time
            stringHash = (stringHash * baseConstant - nums[start - 1] * baseConstantLeftOfMid + nums[
                start + leftOfMid - 1]) % modulus
            if stringHash in seen:
                return start
            seen.add(stringHash)
        return -1

    def longestDupSubstring(self, S):
        stringLength = len(S)
        # convert string to array of integers
        # to implement constant time slice
        nums = [ord(S[i]) - ord('a') for i in range(stringLength)]
        # base value for the rolling hash function
        baseConstant = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2 ** 32

        # binary search, L = repeating string length
        left, right = 1, stringLength
        while left <= right:
            leftOfMid = left + (right - left) // 2
            if self.search(leftOfMid, baseConstant, modulus, stringLength, nums) != -1:
                left = leftOfMid + 1
            else:
                right = leftOfMid - 1

        start = self.search(left - 1, baseConstant, modulus, stringLength, nums)
        return S[start: start + left - 1]
