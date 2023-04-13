## bubbles up the largest element at end
def bubble_sort(elements):
    size = len(elements)

    for i in range(size - 1):
        ## flag to check if list is already sorted
        swapped = False 
        for j in range(size - 1 - i):
            if elements[j] > elements[j+1]:
                ## swap
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
        
        if not swapped:
            break


## bubbles up the largest element at end
def bubble_sort_modified(elements, key):
    size = len(elements)

    for i in range(size - 1):
        ## flag to check if list is already sorted
        swapped = False 
        for j in range(size - 1 - i):
            if elements[j][key] > elements[j+1][key]:
                ## swap
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
        
        if not swapped:
            break



if __name__ == "__main__":
    elements = [5,9,2,1,67,34,88,34]
    elements = [1,2,3,4,2]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    # bubble_sort_modified(elements, key = "name")
    # bubble_sort_modified(elements, key = "transaction_amount")
    bubble_sort_modified(elements, key = "device")
    # bubble_sort(elements)
    print(elements)