# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
  # Your code here
    middle = (start + end) // 2
    if len(arr) == 0:
        return -1
    elif arr[middle] == target:
        return middle

    elif arr[middle] < target:
        # start is the index after the middle
        return binary_search(arr, target, middle+1, end)
    else:
        # the end is the index before the middle
        return binary_search(arr, target, start, middle-1)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


# def agnostic_binary_search(arr, target):
#     # Your code here
#     pass
