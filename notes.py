'''
Recursion is method to solve a problem
1. It means breaking down the problems into small sub-problems until the sub=problems is east to solve
2. it calls itself 
3. in some cases , recursion is so elegant and clean to use however is not always  the most 
efficient choice 



first we have to understand the problems so we can divide them into small problems
THEN , when it comes to implement the code 
we have to know the where is the base , i mean where should our function stop its iteration 
'''


# this loop
def sums_loop(nums):
    sum = 0
    for i in nums:
        sum += i

    return sum


# print(sums_loop([1, 2, 3, 4, 5]))

def sums_recursion(arr):
    # first we check the len of the array
    if len(arr) == 1:
        # we dont need to iterate because we have only one element
        return arr[0]
    else:
        # here we call our function again and agin until it reached the length of 1 to stop
        return arr[0] + sums_recursion(arr[1:])


# print(sums_recursion([1, 2, 3, 4, 5]))

def print_n(n):
    # here we are printing the value of n

    if n < 0:
        # our check base in case the number is 0 then the function stops calling itself
        return
    print(n)
    # repeat until it reached the number 0 to stop
    return print_n(n - 1)


# print_n(5)


'''
There are 3 rules to use the recursive function
1. we have to have a base case to stope our function so we dont run into stack over flow
2. it have to change its state to move forword
3. must call itself



Now , where should i use recursion ?

'''
# Write a recursive search function that receives as input an array
#  of integers and a target integer value. This function should return
#   True if the target element exists in the array, and False otherwise.
# What would be the base case(s) we’d have to consider for implementing this function?
# How should our recursive solution converge on our base case(s)?


def find_target(arr, target):
    # for i in range(0, len(arr)):
    #     if arr[i] == target:
    #         return True
    if len(arr) == 1 and arr[0] == target:
        return True
    elif arr[len(arr) - 1] == target:
        return True
    elif len(arr) > 1:
        return find_target(arr[0:len(arr) - 1], target)
    return False


print(find_target([1, 2, 3, 4], 4))
