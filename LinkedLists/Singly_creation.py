class Node:
    def __init__(self, data = None, next = None) -> None:
        self.data = data 
        self.next = next 
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None 
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node 

    def print(self):
        if self.head is None:
            print("Linked List is empty.")
            return 
        
        itr = self.head 
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next 
        print(llstr)

    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return 

        itr = self.head
        while itr.next:
            itr = itr.next 
        
        itr.next = Node(data, None)

    
    def insert_values(self, data_list):
        self.head = None 
        for data in data_list:
            self.insert_at_end(data)


    def get_length(self):
        count = 0
        itr = self.head 
        while itr:
            count += 1
            itr = itr.next 

        return count 
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next 
        
        count = 0
        itr = self.head 
        while itr:
            if count == index - 1:
                itr.next  = itr.next.next 
                break

            itr = itr.next
            count += 1

    ## insert data value at given index
    def insert_at(self, index, data):
        ## if index is negative or index is more than linked list length
        if index < 0 or index > self.get_length():
            ## raise exception
            raise Exception("Invalid Index")
        
        ## if index is zero
        if index == 0:
            ## insert at begining
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head 
        ##  Iterate through list
        while itr:
            ## we want to change the pointers when we are one index before the index 
            ## where we want to insert the value
            if count == index - 1:
                ## create a node with data value and assign next pointer to the next of itr node
                node = Node(data, itr.next)
                ## assign the node value to itr next
                itr.next = node 
                break 

            itr = itr.next 
            count += 1  


    ## Insert the data value after a given data value from linked list
    def insert_after_value(self, data_after, data_to_insert):
        ## if linked list exists
        if self.head:
            ## initialize the list head to itr for iteration
            itr = self.head 
            ## Iterate through linked list
            while itr:
                ## if data of current node is the data, after which we want to insert the data
                if itr.data == data_after:
                    ## create the node
                    node = Node(data_to_insert, itr.next)
                    ## assign the node to the next pointer of itr node
                    itr.next = node 
                    break
                ## jump to next node
                itr = itr.next 
                

    ## Remove given data value
    def remove_by_value(self, data_to_delete):
        ## if list exist
        if self.head:
            itr = self.head 
            ## Iterate through list
            while itr:
                ## check if next node data to be deleted
                if itr.next.data == data_to_delete:
                    ## delete next node by pointing next to next node
                    itr.next = itr.next.next
                    break
                ## jump to next node
                itr = itr.next    

    ## reverse linked list
    def reverse(self):
        
        if self.head:
            previous = None
            current = self.head
            while current:
                ## next is pointing the next node of current node
                next = current.next
                ## make pointer of current node to point previous node
                current.next = previous
                ## increment both pointers 
                previous = current
                current = next 

            self.head = previous 
    

    ## reverse using recursion
    def reverse_recursion(self):
        head = self.head
        ## if list does not exist or have only one element 
        if self.head is None or self.head.next is None:
            return self.head 
        
        ## reverse the rest list
        rest = self.reverse_recursion(head.next)

        ## put first element at end
        head.next.next = head 
        head.next = None 

        ## fix header pointer
        return rest


    ## 




if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(23)
    # ll.insert_at_begining(71)
    # ll.insert_at_end(100)
    # ll.insert_at_end(1000)
    ll.insert_values([10,20,30,40,50])
    # ll.print()
    # ll.remove_at(2) ## index
    # ll.insert_at(2, 100)
    # ll.insert_after_value(20, 10000)
    # ll.print()
    # ll.remove_by_value(10000)
    # ll.print()
    # print("Length of the linked list : ",ll.get_length())

    ll.reverse()
    ll.print()
    ll.reverse_recursion()
    ll.print()
