##############################
# Code from task 14_1
##############################

class Tree:

    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.element)

    def push_from_list(self, list_):
        for element in list_:
            self.insert(element)

    # Insert method to create nodes
    def insert(self, element):
        if self.element:
            if element < self.element:
                if self.left is None:
                    self.left = Tree(element)
                else:
                    self.left.insert(element)
            elif element > self.element:
                if self.right is None:
                    self.right = Tree(element)
                else:
                    self.right.insert(element)
        else:
            self.element = element

    # findval method to compare the element with nodes
    def findval(self, find_val):
        if find_val < self.element:
            if self.left is None:
                return str(find_val) + " Not Found"
            return self.left.findval(find_val)
        elif find_val > self.element:
            if self.right is None:
                return str(find_val) + " Not Found"
            return self.right.findval(find_val)
        else:
            print(str(self.element) + ' is found')

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        if self.element:
            print(self.element),
        if self.right:
            self.right.print_tree()

################################
    # Finding the minimum
################################
    def get_min_node(self):
         if self.left is None:
             return self.element

         return self.left.get_min_node()

#####################################
    # Finding the maximum
####################################

    def get_max_node(self):
         if self.right is None:
             return self.element

         return self.right.get_max_node()

my_btree = Tree(6)
my_btree.push_from_list([12, 5, 41, 18, 4, 57, 11, 72])
my_btree.print_tree()
print("--------------------------")
print(f"Minimum value in Tree = {my_btree.get_min_node()}\nMaximum value in Tree = {my_btree.get_max_node()}")

