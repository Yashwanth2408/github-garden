# Sorting algorithms — grown by the garden one function at a time

def counting_sort(arr, max_val=None):
    """Counting sort for non-negative integers. O(n + k) time and space."""
    if not arr:
        return arr
    if max_val is None:
        max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    result = []
    for num, freq in enumerate(count):
        result.extend([num] * freq)
    return result
