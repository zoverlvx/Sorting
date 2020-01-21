def quicksort(arr):
    return quicksort_helper(arr, 0, len(arr))

def quicksort_helper(arr, low, high):
    # Pick a pivot and move it until everything
    # on the left is smaller & everything on the right is greater
    if low >= high:
        return

    pivot_index = high - 1
    for i in range(high - 1, low - 1, -1):
        if arr[pivot_index] < arr[i]:
            # do double-swap
            arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
            arr[i], arr[pivot_index - 1] = arr[pivot_index - 1], arr[i]
            pivot_index -= 1
    quicksort_helper(arr, low, pivot_index)
    quicksort_helper(arr, pivot_index + 1, high)
