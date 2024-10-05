def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Find the middle point to divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])   # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Merge the two halves while comparing elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # If there are remaining elements in left, append them
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    # If there are remaining elements in right, append them
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

# Example usage
if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print("Original array:", data)
    sorted_data = merge_sort(data)
    print("Sorted array:", sorted_data)