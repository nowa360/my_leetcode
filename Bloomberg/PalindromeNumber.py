def isPalindrome(x):
    """
    9. Palindrome Number
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False

    x_clone = x
    reverse = 0
    while x_clone:
        reverse = x_clone % 10 + reverse * 10
        x_clone /= 10

    return x == reverse
