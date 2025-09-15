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

def binary_search_leftmost(arr, target):
    """Find leftmost occurrence in sorted array. O(log n) time."""
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low if low < len(arr) and arr[low] == target else -1

def heap_sort(arr):
    """Heapsort. O(n log n) time, O(1) space. Not stable."""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)
    return arr


def _heapify(arr, n, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)

def merge_sort(arr):
    """Merge sort. O(n log n) time, O(n) space. Stable."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result

def bubble_sort(arr):
    """Bubble sort. O(n²) time, O(1) space. Stable."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def quick_sort(arr, low=None, high=None):
    """Quicksort. O(n log n) average, O(n²) worst, O(log n) space."""
    if low is None:
        low, high = 0, len(arr) - 1
    if low < high:
        p = _partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    return arr


def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def shell_sort(arr):
    """Shell sort with Knuth sequence. O(n^1.5) average, O(1) space."""
    n = len(arr)
    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1
    while gap >= 1:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 3
    return arr

def binary_search(arr, target):
    """Binary search in sorted array. O(log n) time, O(1) space.
    Returns index if found, -1 otherwise."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def radix_sort(arr):
    """Radix sort for non-negative integers. O(d*(n+b)) time, stable."""
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = _counting_sort_digit(arr, exp)
        exp *= 10
    return arr


def _counting_sort_digit(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10
    for num in arr:
        count[(num // exp) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for num in reversed(arr):
        d = (num // exp) % 10
        count[d] -= 1
        output[count[d]] = num
    return output

def insertion_sort(arr):
    """Insertion sort. O(n²) worst, O(n) best, O(1) space. Stable."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
