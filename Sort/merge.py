# def merge_sorted_arrays(a, b):
#     sorted_list = []
#     len_a = len(a)
#     len_b = len(b)

#     i = j = 0

#     while i < len_a and j < len_b:
#         if a[i] <= b[j]:
#             sorted_list.append(a[i])
#             i += 1
#         else:
#             sorted_list.append(b[j])
#             j += 1

#     while i < len_a:
#         sorted_list.append(a[i])
#         i += 1
    
#     while j < len_b:
#         sorted_list.append(b[j])
#         j += 1

    
#     return sorted_list


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr 
    
#     mid = len(arr)//2

#     left = arr[:mid]
#     right = arr[mid:]

#     left_list = merge_sort(left)
#     right_list = merge_sort(right)

#     return merge_sorted_arrays(left_list, right_list)


## inplace
def merge_sorted_arrays(a, b, arr):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            # sorted_list.append(a[i])
            arr[k] = a[i]
            i += 1
            k += 1
        else:
            # sorted_list.append(b[j])
            arr[k] = b[j]
            j += 1
            k += 1

    while i < len_a:
        # sorted_list.append(a[i])
        arr[k] = a[i]
        i += 1
        k += 1
    
    while j < len_b:
        # sorted_list.append(b[j])
        arr[k] = b[j]
        j += 1
        k += 1
    
    return sorted_list

def merge_sort(arr):
    if len(arr) <= 1:
        return arr 
    
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_sorted_arrays(left, right, arr)



## inplace
def merge_sorted_arrays_keys(a, b, arr, key = None):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    print('A and B : ', a, b)

    while i < len_a and j < len_b:
        if a[i][key] <= b[j][key]:
            # sorted_list.append(a[i])
            arr[k] = a[i][key]
            i += 1
            k += 1
        else:
            # sorted_list.append(b[j])
            arr[k] = b[j][key]
            j += 1
            k += 1

    while i < len_a:
        # sorted_list.append(a[i])
        arr[k] = a[i][key]
        i += 1
        k += 1
    
    while j < len_b:
        # sorted_list.append(b[j])
        arr[k] = b[j][key]
        j += 1
        k += 1
    
    return sorted_list




def merge_sort_keys(arr, key, descending=False):
    if len(arr) <= 1:
        return arr 
    
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort_keys(left, key)
    merge_sort_keys(right, key)

    merge_sorted_arrays_keys(left, right, arr, key)



if __name__ == '__main__':
    # test_cases = [
    #     [10, 3, 15, 7, 8, 23, 98, 29],
    #     [],
    #     [3],
    #     [9,8,7,2],
    #     [1,2,3,4,5]
    # ]

    # for arr in test_cases:
    #     merge_sort(arr)
    #     print(arr)

    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    merge_sort_keys(elements, "name", descending=False)
        