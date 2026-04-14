def merge_sort(arr):
    """
    Sorts a list in ascending order using the Merge Sort algorithm.

    Time Complexity: O(n log n), where n is the number of elements in the list.
    Space Complexity: O(n), due to the use of temporary arrays during merging.

    Args:
        arr (list): The list to be sorted.

    Returns:
        list: A new sorted list.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test cases
if __name__ == "__main__":
    test_cases = [
        [],
        [1],
        [5, 2, 9, 1, 5, 6],
        [3, 2, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [7, 7, 7, 7],
    ]

    for idx, case in enumerate(test_cases):
        sorted_case = merge_sort(case)
        print(f"Test case {idx+1}: Input: {case} -> Sorted: {sorted_case}")