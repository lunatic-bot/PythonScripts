class TreeNode:
    def __init__(self, data):
        self.data = data
        self.childern = []
        self.parent = None

    
    def add_child(self, child):
        child.parent = self
        self.childern.append(child)

    ## count ancestors
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level
    

    def print_tree(self):
        spaces = " " * self.get_level() * 3 
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        # if len(self.childern) > 0:
        if self.childern:
            for child in self.childern:
                # print(child.data)
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")
    # laptop = TreeNode("Laptop")
    # root.add_child(laptop)
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    print(tv.get_level())

    return root

    
if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    print(root.get_level())
    pass