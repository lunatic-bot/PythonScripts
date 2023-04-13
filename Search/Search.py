
from util import time_it

@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    # all_indices = []

    while left_index <= right_index:
        ## get mid index
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        ## if mid number is the number we were searching
        if mid_number == number_to_find:
            # all_indices.append(mid_index)
            return mid_index

        ## get left or right index according to number searched,
        ## set left and right index accordingly
        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    # print('All possible indices of searched value : ', all)

    return -1


## recursive function for binary search
def binary_search_recursive(numbers_list, number_to_search, left_index, right_index):
    ## if right index is less than left at any time return -1
    if right_index < left_index:
        return -1
    
    ## get mid index
    mid_index = (left_index + right_index) // 2
    ## if mid index is larger than the length or -1, return -1
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1
    
    ## get mid element
    mid_number = numbers_list[mid_index]
    ## if mid number is the number we were searching
    if mid_number == number_to_search:
        return mid_index
    
    ## get left or right index according to number searched
    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    ## call function recursively
    return binary_search_recursive(numbers_list, number_to_search, left_index, right_index)
    

## find all occurances of searched value
def find_all_occurances(numbers, number_to_find):
    ## find index using binary search
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    ## Iterate till index zero to find other occurances
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    ## Iterate till index len(numbers) - 1 to find other occurances
    while i < len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)



if __name__ == '__main__':
    # numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    # number_to_find = 67

    numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15  

    # numbers_list = [i for i in range(100000001)]
    # number_to_find = 100000000

    # index = linear_search(numbers_list, number_to_find)

    index = find_all_occurances(numbers_list, number_to_find)

    # index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f"Number found at index {index} using binary search")