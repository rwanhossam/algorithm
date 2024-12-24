def heapify(arr, n, i):
    """
    Heapify subtree rooted at index i.
    Args:
        arr: array to heapify
        n: size of heap
        i: root index of subtree
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Compare root with left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Compare root with right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Sort array using heap sort algorithm.
    Args:
        arr: array to sort
    Returns:
        sorted array
    """
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)
    
    return arr

# Example usage
if __name__ == "__main__":
    # Test the implementation
    test_array = [12, 11, 13, 5, 6, 7]
    print("Original array:", test_array)
    sorted_array = heap_sort(test_array)
    print("Sorted array:", sorted_array)
Last edited 8 minutes ago



