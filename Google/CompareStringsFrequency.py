"""
Naive approach to:
https://leetcode.com/discuss/interview-question/352458/

"""


def compare_st_frequency(a, b):
    def is_more_frequent(str1, str2):
        min_a, min_b = ord('z'), ord('z')
        a_count, b_count = 0, 0
        for ch in str1:
            if ord(ch) < min_a:
                min_a = ord(ch)
                a_count = 1
            elif ord(ch) == min_a:
                a_count += 1
        for ch in str2:
            if ord(ch) < min_b:
                min_b = ord(ch)
                b_count = 1
            elif ord(ch) == min_b:
                b_count += 1
        return a_count >= b_count

    res = [0] * len(b)

    for i, str_b in enumerate(b):
        count = 0
        for str_a in a:
            if not is_more_frequent(str_a, str_b):
                count += 1
        res[i] = count

    return res


A1 = ["abcd", "aabc", "bd"]
B1 = ["aaa", "aa"]
print(compare_st_frequency(A1, B1))  # expects [3, 2]
