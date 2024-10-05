def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, no need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print("Original array:", data)
    bubble_sort(data)
    print("Sorted array:", data)