def binary_search(arr, target):
    """
    Performs binary search to find the index of 'target' in a sorted list 'arr'.

    Args:
        arr (list): Sorted list of elements.
        target: Element to search for.

    Returns:
        int: Index of 'target' if found, else -1.

    Complexity:
        Best-case: O(1)   - Target is at the middle.
        Average-case: O(log n)
        Worst-case: O(log n)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test cases
if __name__ == "__main__":
    arr1 = [1, 3, 5, 7, 9, 11]
    arr2 = [2, 4, 6, 8, 10]
    arr3 = []
    arr4 = [5]

    print(binary_search(arr1, 7))    # Output: 3
    print(binary_search(arr1, 1))    # Output: 0
    print(binary_search(arr1, 11))   # Output: 5
    print(binary_search(arr1, 12))   # Output: -1
    print(binary_search(arr2, 6))    # Output: 2
    print(binary_search(arr3, 1))    # Output: -1
    print(binary_search(arr4, 5))    # Output: 0
    print(binary_search(arr4, 2))    # Output: -1