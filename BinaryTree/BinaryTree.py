class Node:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def set_right(self, node):
        self.right = node

    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def get_data(self):
        return self.data

class BinaryTree:

    def __init__(self, data=None):
        if data is not None:
            self.root = Node(data)
        else:
            self.root = None

    def get_root(self):
        return self.root

    #Insert data into the binary tree
    def insert(self, data):
        #Check if tree has root node
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_into_node(data, self.root)

    #Insert data at a given node
    def insert_into_node(self, data, node):
        left = node.get_left()
        right = node.get_right()
        node_data = node.get_data()

        #Check if node already exists
        if node_data == data:
            return

        #If node is less than current node, insert into left otherwise right
        if data < node_data:
            if left is not None:
                self.insert_into_node(data, left)
            else:
                node.set_left(Node(data))
        else:
            if right is not None:
                self.insert_into_node(data, right)
            else:
                node.set_right(Node(data))

    def print(self):
        self.print_tree(self.root, 0)

    def print_tree(self, current, indent):
        if current is not None:
            print(indent * " " + "-> " + str(current.get_data()))
            left = current.get_left()
            self.print_tree(left, indent + 4)
            right = current.get_right()
            self.print_tree(right, indent + 4)
