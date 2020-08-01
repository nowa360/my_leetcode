"""
July 29 Challenge - Best Time to Buy and Sell Stock with Cool-down

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell
 one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    if not prices or len(prices) == 0:
        return 0

    dp = [0 for _ in xrange(len(prices))]

    max_diff = float('-inf')

    for i in xrange(len(prices)):

        if i < 2:
            max_diff = max(max_diff, -prices[i])

        if i == 0:
            dp[i] = 0
        elif i == 1:
            dp[i] = max(prices[1] - prices[0], 0)
        else:
            dp[i] = max(dp[i - 1], max_diff + prices[i])
            max_diff = max(max_diff, dp[i - 2] - prices[i])

    return dp[-1]
