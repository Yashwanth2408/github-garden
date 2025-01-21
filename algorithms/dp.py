# Dynamic programming — grown by the garden one function at a time

import bisect


def lis_length(arr):
    """Longest Increasing Subsequence length. O(n log n) — patience sorting."""
    tails = []
    for num in arr:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)

def coin_change(coins, amount):
    """Minimum coins for amount. O(n * amount). Returns -1 if impossible."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_ways(coins, amount):
    """Count distinct ways to make amount. O(n * amount)."""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]
