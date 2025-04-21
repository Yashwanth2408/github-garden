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

def kadane(arr):
    """Maximum subarray sum (Kadane). O(n) time, O(1) space.
    Returns (max_sum, start, end)."""
    best = curr = arr[0]
    best_s = best_e = tmp_s = 0
    for i in range(1, len(arr)):
        if curr + arr[i] < arr[i]:
            curr = arr[i]; tmp_s = i
        else:
            curr += arr[i]
        if curr > best:
            best = curr; best_s = tmp_s; best_e = i
    return best, best_s, best_e

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

def lcs(s, t):
    """Longest Common Subsequence. O(mn) time and space.
    Returns the subsequence string."""
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i-1][j-1] + 1 if s[i-1] == t[j-1] else max(dp[i-1][j], dp[i][j-1])
    seq, i, j = [], m, n
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            seq.append(s[i-1]); i -= 1; j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(seq))

def knapsack_01(weights, values, capacity):
    """0/1 Knapsack. O(n * capacity) time and space.
    Returns (max_value, list_of_selected_indices)."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
    selected, w = [], capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i - 1)
            w -= weights[i-1]
    return dp[n][capacity], list(reversed(selected))

def edit_distance(s, t):
    """Levenshtein edit distance. O(mn) time and space."""
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i-1][j-1] if s[i-1] == t[j-1] else 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

def knapsack_01(weights, values, capacity):
    """0/1 Knapsack. O(n * capacity) time and space.
    Returns (max_value, list_of_selected_indices)."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
    selected, w = [], capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i - 1)
            w -= weights[i-1]
    return dp[n][capacity], list(reversed(selected))

def knapsack_01(weights, values, capacity):
    """0/1 Knapsack. O(n * capacity) time and space.
    Returns (max_value, list_of_selected_indices)."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
    selected, w = [], capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i - 1)
            w -= weights[i-1]
    return dp[n][capacity], list(reversed(selected))

def knapsack_01(weights, values, capacity):
    """0/1 Knapsack. O(n * capacity) time and space.
    Returns (max_value, list_of_selected_indices)."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
    selected, w = [], capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i - 1)
            w -= weights[i-1]
    return dp[n][capacity], list(reversed(selected))
