# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # creates new array in order to not mutate the original
    new_array = [] + arr
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): # O(n^2)
        minIndex = i
        for j in range(i + 1, len(new_array)):
            if new_array[j] < new_array[minIndex]:
                minIndex = j
        if minIndex != i:
            new_array[i], new_array[minIndex] = new_array[minIndex], new_array[i]

    return new_array


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    new_array = [] + arr
    length = len(new_array)
    for i in range(length):
        for j in range(0, length - i - 1):
            if new_array[j] > new_array[j + 1]:
                new_array[j], new_array[j+1] = new_array[j+1], new_array[j]
    return new_array

# Optimized bubble sort: (mutates)
def bubbleSort(A):
    length = len(A)

    # traverse through all array elements
    for i in range(n):
        swapped = False

        # last i elements are already in place
        for j in range(0, length - i - 1):

            # traverse the list from 0 to length - i - 1
            # swap if the element found is greater than the next element
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True
        # if no two elements were swapped by inner loop, then break
        if swapped == False:
            break

# https://www.youtube.com/watch?v=CX_kHnEvFZ8
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
