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
    

    # def print_tree(self):
    #     spaces = " " * self.get_level() * 3 
    #     prefix = spaces + "|__" if self.parent else ""
    #     print(prefix + self.data)
    #     # if len(self.childern) > 0:
    #     if self.childern:
    #         for child in self.childern:
    #             # print(child.data)
    #             child.print_tree()

    
    def print_tree(self, print_type):

        spaces = " " * self.get_level() * 3 
        prefix = spaces + "|__" if self.parent else ""

        data_value = self.data 
        splits = data_value.split(' (')
        # print(splits)
        if print_type == "name":
            print(prefix + splits[0])
        elif print_type == "designation":
            print(prefix + splits[1].replace(')', ''))
        else:
            print(prefix + self.data)
            # if len(self.childern) > 0:
        if self.childern:
            for child in self.childern:
                # print(child.data)
                child.print_tree(print_type)


def build_management_tree():
    root = TreeNode("Nilupul (CEO)")
    # laptop = TreeNode("Laptop")
    # root.add_child(laptop)
    cto = TreeNode("Chinmay (CTO)")
    infra = TreeNode("Viswa (Infra Head)")
    infra.add_child(TreeNode("Dhaval (Cloud Manager)"))
    infra.add_child(TreeNode("Abhijeet (App Manager)"))
    cto.add_child(infra)

    cto.add_child(TreeNode("Aamir (Application Head)"))
    
    HR = TreeNode("Gels (HR Head)")
    HR.add_child(TreeNode("Peter (Recruitment Manager)"))
    HR.add_child(TreeNode("Waqas (Policy Manager)"))


    root.add_child(cto)
    root.add_child(HR)


    # print(tv.get_level())

    return root


if __name__ == '__main__':
    root_node = build_management_tree()
    # root_node.print_tree("name")
    # root_node.print_tree("name") # prints only name hierarchy
    # root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
    
# if __name__ == "__main__":
#     root = build_product_tree()
    
#     print(root.get_level())
#     pass