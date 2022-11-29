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
    # Removing elements
################################

    def remowe_element(self, root, node_elem):

        if root.element == node_elem:
            if not root.right: return root.left

            if not root.left: return root.right

            if root.left and root.right:
                temp = root.right
                while temp.left: temp = temp.left
                root.element = temp.element
                root.right = self.remove_element(root.right, root.element)

        elif root.element > node_elem:
            root.left = self.remowe_element(root.left, node_elem)
        else:
            root.right = self.remowe_element(root.right, node_elem)

        return root

my_btree = Tree(6)
my_btree.push_from_list([12, 5, 41, 18, 4, 57, 11, 72])
print("Full Tree")
my_btree.print_tree()

my_btree.remowe_element(my_btree,5)
print("Tree with removed element ")
my_btree.print_tree()
