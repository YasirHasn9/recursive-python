# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    merge_sort = merge_sort(merged_arr)
    return merge_sort

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    if len(arr) > 1:
        # find the middle of the list
        mid = len(arr)//2
        # divide it into 2 halves
        L = arr[:mid]
        R = arr[mid:]


# divide and conquer each list
        merge_sort(L)
        merge_sort(R)

# start form 0 index in each list and compar it to the other index in the other lisrt
        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            # loop over every index in the left and compar it to the right
            # and push the item to the main list
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                # loop over every index in the right and compar it to the left
                # and push the item to the main list
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
