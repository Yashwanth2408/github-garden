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
