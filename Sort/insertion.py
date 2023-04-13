## Insertion sort
def insertion_sort(elements):
    for i in range(1, len(elements)):
        ## get an element
        anchor = elements[i]
        ## set j on index one less than i
        j = i - 1
        ## while anchor is less than elements at j index, 
        while j >= 0 and anchor < elements[j]:
            ## swap consecutive elements
            elements[j + 1] = elements[j]
            ## decrement j
            j = j - 1

        ## put anchor at its right position
        elements[j+1] = anchor


# ## median of the list so far on each new element.
# def running_median(elements):
#     for i in range(1, len(elements)):
#         ## get an element
#         anchor = elements[i]
#         ## set j on index one less than i
#         j = i - 1
#         ## while anchor is less than elements at j index, 
#         while j >= 0 and anchor < elements[j]:
#             ## swap consecutive elements
#             elements[j + 1] = elements[j]
#             ## decrement j
#             j = j - 1

#         ## put anchor at its right position
#         elements[j+1] = anchor

#         print(elements[0:i])
#         # print(sum(elements[0:i])/i)

#         count = i

#         if count % 2 == 1:
#             print(f"Median of {elements[0:i]} : {elements[(count)//2]}")
#         else:
#             i1 = count//2
#             i2 = (count//2) - 1
#             print(f"Median of {elements[0:i]} : {(elements[i1] + elements[i2])/2}")



# if __name__ == '__main__':
#     elements = [11,9,29,7,2,15,28]
    # insertion_sort(elements)
    # print(elements)
    # #
    # tests = [
    #     [11,9,29,7,2,15,28],
    #     [3, 7, 9, 11],
    #     [25, 22, 21, 10],
    #     [29, 15, 28],
    #     [],
    #     [6]
    # ]

    # for elements in tests:
    #     insertion_sort(elements)
    #     print(f'sorted array: {elements}')
    # elements = [2, 1, 5, 7, 2, 0, 5]
    # running_median(elements)

def place_to_insert(array, key):
    index = 0
    for i in array:
        if i > key:
            break
        else:
            index += 1
    return index


def insert_to_sorted(array, key):
    index = place_to_insert(array, key)
    return array[0:index]+[key]+array[index:]


if __name__ == "__main__":
    array = [2, 1, 5, 7, 2, 0, 5]

    stream = []
    k = 0

    count = 0
    while(True) and k < len(array):
        i = array[k]
        k += 1
        count += 1
        stream = insert_to_sorted(stream, i)
        if count % 2 == 1:
            print(f"Median of {stream} : {stream[(count)//2]}")
        else:
            i1 = count//2
            i2 = (count//2) - 1
            print(f"Median of {stream} : {(stream[i1] + stream[i2])/2}")