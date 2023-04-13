class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = None 
        self.right = None  
        self.height = 0

## get height of a node
def get_height(node):
    if node is None:
        return 0 
    
    return node.height

## get balance factor of a node in AVL tree
def get_balance_factor(node):
    if node is None:
        return 0
    
    return get_height(node.left) - get_height(node.right)


## right rotate 
def right_rotate(nodeY):
    nodeX = nodeY.left
    nodeT2 = nodeX.right

    nodeX.right = nodeY
    nodeY.left = nodeT2 

    nodeY.height = max(get_height(nodeY.right), get_height(nodeY.left)) + 1
    nodeX.height = max(get_height(nodeX.right), get_height(nodeX.left)) + 1

    return nodeY



## left rotate 
def left_rotate(nodeX):
    nodeY = nodeX.right
    nodeT2 = nodeY.left

    nodeY.left = nodeX
    nodeX.right = nodeT2

    nodeY.height = max(get_height(nodeY.right), get_height(nodeY.left)) + 1
    nodeX.height = max(get_height(nodeX.right), get_height(nodeX.left)) + 1

    return nodeY


def bst_insertion(node, val):
    if node is None:
        return TreeNode(val)
    
    if val < node.val:
        node.left = bst_insertion(node.left, val)

    elif val > node.val:
        node.right = bst_insertion(node.right, val)

    # return node
    node.height = 1 + max(get_height(node.right), get_height(node.left))
    balanceFactor = get_balance_factor(node)

    ## left left case 
    if balanceFactor > 1 and val < node.left.val:
        return right_rotate(node)

    ## right right case
    if balanceFactor < -1 and val >  node.right.val:
        return left_rotate(node)

    ## left right case
    if balanceFactor > 1 and val > node.left.val:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    ## right left case
    if balanceFactor < -1 and val < node.right.val:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node
        

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end = ' ')
        inorder(root.right)

    

if __name__ == "__main__":
    root = TreeNode(10)
    bst_insertion(root, 15)
    bst_insertion(root, 12)
    bst_insertion(root, 5)
    bst_insertion(root, 7)
    bst_insertion(root, 6)
    bst_insertion(root, 9)
    bst_insertion(root, 11)

    inorder(root)


