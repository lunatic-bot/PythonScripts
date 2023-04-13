## deletion
# 1. Deletion of a node with no child 
# remove the node

# 2. Deletion of a node with one child
# remove and move child upper

# 3. Deletion of a node with two children
# delete and replace with smallest value from right subtree
# delete and replace with largest value from left subtree

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

    ## add child to a node 
    def add_child(self, data):
        ## if value is same as data value of node
        if data == self.data:
            return
        
        
        if data < self.data:
            ## add in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            ## add in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def inorder_traversal(self):
        elements = []

        ## visit the left subtree
        if self.left:
            elements += self.left.inorder_traversal()

        ## data of node
        elements.append(self.data)

        ## visit the right subtree
        if self.right:
            elements += self.right.inorder_traversal()

        return elements
    
    ## search a value in binary search tree
    def search(self, val):
        if self.data == val:
            # print("Value is equal to node")
            return True 
        
        # print(self.data)
        
        ## search in left subtree
        if val < self.data:
            if self.left:
                # print('value is less than node, going to left')
                return self.left.search(val)
            else:
                return False
        
        ## search in right subtree
        if val > self.data:
            if self.right:
                # print('value is grater than node, going to right')
                return self.right.search(val)
            else:
                return False
            

    ## EXERCISE
    def find_min(self):
        ## left most element will be smallest element 
        if self.left:
            return self.left.find_min()
        
        return self.data
    
        # if self.left is None:
        #     return self.data
        # return self.left.find_min()


    ## find largest element
    def find_max(self):
        ## right most element will be largest element 
        if self.right:
            return self.right.find_max()
        
        return self.data

    ## calculate sum of all node values
    def calculate_sum(self):
        ## sum of left subtree
        left_sum = self.left.calculate_sum() if self.left else 0
        ## sum of right subtree
        right_sum = self.right.calculate_sum() if self.right else 0
        ## return over all sum for current level
        return self.data + left_sum + right_sum
            

    ## pre order
    def pre_order_traversal(self):
        elements = []

        ## data of node
        elements.append(self.data)

        ## visit the left subtree
        if self.left:
            elements += self.left.pre_order_traversal()

        ## visit the right subtree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    ## post order
    def post_order_traversal(self):
        elements = []

        
        ## visit the left subtree
        if self.left:
            elements += self.left.post_order_traversal()

        ## visit the right subtree
        if self.right:
            elements += self.right.post_order_traversal()

        ## data of node
        elements.append(self.data)

        return elements
    

    ## delete the value from BST
    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        
        else:
            ## if leaf node
            if self.left is None and self.right is None:
                return None
            
            ## if there is only right subtree
            if self.left is None:
                return self.right
            
            ## if there is only left subtree
            if self.right is None:
                return self.left 
            
            ## if both subtree
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


    ## delete the value from BST
    def delete_using_max(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        
        else:
            ## if leaf node
            if self.left is None and self.right is None:
                return None
            
            ## if there is only right subtree
            if self.left is None:
                return self.right
            
            ## if there is only left subtree
            if self.right is None:
                return self.left 
            
            ## if both subtree
            min_val = self.left.find_max()
            self.data = min_val
            self.left = self.left.delete(min_val)

        return self


    
def build_tree(elements):
    ## create root node with first data value
    root = BinarySearchTreeNode(elements[0])
    ## add all otehr nodes
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root
    

## BST
## --> Used for sorting elements of a list
## --> used for getting set for a list

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    # numbers = [1]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.inorder_traversal())
    # numbers_tree.delete(20)
    numbers_tree.delete_using_max(23)
    print(numbers_tree.inorder_traversal())
    # print(numbers_tree.search(180))
    # print(numbers_tree.find_min())
    # print(numbers_tree.find_max())
    # print(numbers_tree.calculate_sum())
    # print(numbers_tree.pre_order_traversal())
    # print(numbers_tree.post_order_traversal())


