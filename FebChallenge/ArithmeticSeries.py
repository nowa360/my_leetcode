"""
Feb 18 Challenge - Arithmetic Slices

A sequence of numbers is called arithmetic if it consists of at least three elements and
if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q)
such that 0 <= P < Q < N.

A slice (P, Q) of the array A is called arithmetic if the sequence:
A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

"""


def numberOfArithmeticSlices(A):
    """
    :type A: List[int]
    :rtype: int
    """
    if len(A) < 3:
        return 0

    dp = [0 for i in xrange(len(A))]

    saved_diff = None
    plus_factor = 0

    for i in xrange(len(A) - 2):
        if (A[i + 1] - A[i]) != (A[i + 2] - A[i + 1]):
            plus_factor = 0
            dp[i + 2] = dp[i + 1]

        else:
            if saved_diff == (A[i + 2] - A[i + 1]):
                plus_factor += 1
            else:
                plus_factor = 1
                saved_diff = A[i + 2] - A[i + 1]

            dp[i + 2] = dp[i + 1] + plus_factor

    return dp[-1]
