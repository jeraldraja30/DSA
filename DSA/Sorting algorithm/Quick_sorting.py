def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2] 
         # Choosing the middle element as the pivot
        left = [x for x in arr if x < pivot] 
         # Elements less than the pivot
        middle = [x for x in arr if x == pivot]
         # Elements equal to the pivot
        right = [x for x in arr if x > pivot] 
         # Elements greater than the pivot
        return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print("Original array:", data)
    sorted_data = quick_sort(data)
    print("Sorted array:", sorted_data)