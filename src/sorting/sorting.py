# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    i, j = 0, 0
    curr = 0

    # Your code here
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[curr] = arrA[i]
            i += 1
            curr += 1

        else:
            merged_arr[curr] = arrB[j]
            j += 1
            curr += 1

    while i < len(arrA):
        merged_arr[curr] = arrA[i]
        i += 1
        curr += 1

    while j < len(arrB):
        merged_arr[curr] = arrB[j]
        j += 1
        curr += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):

    if len(arr) > 1:

        middle = len(arr)//2
        arr1 = merge_sort(arr[:middle])
        arr2 = merge_sort(arr[middle:])
        return merge(arr1, arr2)

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
