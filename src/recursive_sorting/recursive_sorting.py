# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( A, B ):
    #elements = len( arrA ) + len( arrB )
    #merged_arr = [0] * elements
    # TO-DO
    merged_arr = A + B 
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( A ):
    # TO-DO
    if len(A) > 1:
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]

        # recursion
        merge_sort(L)
        merge_sort(R)

        i=0
        j=0
        k=0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
    return A



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
