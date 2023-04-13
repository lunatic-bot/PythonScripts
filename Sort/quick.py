## quick sort
## swap elements
def swap(a, b, arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

## devide and conquer
def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    # pass
    # start = pivot_index + 1
    # end = len(elements) - 1

    while start < end:
        ## increase start till we find an element grater than pivot
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        ## decrease end till we find an element less than pivot
        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


# // Divides array into two partitions
# algorithm partition(A, lo, hi) is 
#   pivot := A[hi] // Choose the last element as the pivot

#   // Temporary pivot index
#   i := lo - 1

#   for j := lo to hi - 1 do 
#     // If the current element is less than or equal to the pivot
#     if A[j] <= pivot then 
#       // Move the temporary pivot index forward
#       i := i + 1
#       // Swap the current element with the element at the temporary pivot index
#       swap A[i] with A[j]

#   // Move the pivot element to the correct pivot position (between the smaller and larger elements)
#   i := i + 1
#   swap A[i] with A[hi]
#   return i // the pivot index


def lomuto_partition(elements, start, end):
    ## always selects last element as pivot
    pivot = elements[end]

    ## temporary pivot index
    i = start - 1

    for j in range(start, end):
        ## If the current element is less than or equal to the pivot
        if elements[j] <= pivot:
            ## Move the temporary pivot index forward
            i += 1
            ## Swap the current element with the element at the temporary pivot index
            swap(i, j, elements)
    
    
    ## Move the pivot element to the correct pivot position (between the smaller and larger elements)
    i += 1
    swap(i, end, elements)
    ## the pivot index
    return i

## quick sort
def quick_sort(elements, start, end):
    if start < end or start < 0:
        # pi = partition(elements, start, end)
        pi = lomuto_partition(elements, start, end)
        ## left partition
        quick_sort(elements, pi + 1, end)
        ## right partition
        quick_sort(elements, start, pi - 1)



if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements) - 1)
        print(elements)