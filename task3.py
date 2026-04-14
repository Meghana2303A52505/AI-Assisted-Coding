import random

def quick_sort(arr):
    """
    Sorts an array using the Quick Sort algorithm (recursive).
    Args:
        arr (list): List of elements to sort.
    Returns:
        list: Sorted list.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(arr):
    """
    Sorts an array using the Merge Sort algorithm (recursive).
    Args:
        arr (list): List of elements to sort.
    Returns:
        list: Sorted list.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted lists into one sorted list.
    Args:
        left (list): Sorted left half.
        right (list): Sorted right half.
    Returns:
        list: Merged sorted list.
    """
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

if __name__ == "__main__":
    # Generate test lists
    random_list = [random.randint(1, 100) for _ in range(10)]
    sorted_list = sorted(random_list)
    reverse_sorted_list = sorted(random_list, reverse=True)

    print("Original random list:", random_list)
    print("Quick Sort:", quick_sort(random_list))
    print("Merge Sort:", merge_sort(random_list))

    print("\nOriginal sorted list:", sorted_list)
    print("Quick Sort:", quick_sort(sorted_list))
    print("Merge Sort:", merge_sort(sorted_list))

    print("\nOriginal reverse-sorted list:", reverse_sorted_list)
    print("Quick Sort:", quick_sort(reverse_sorted_list))
    print("Merge Sort:", merge_sort(reverse_sorted_list))




