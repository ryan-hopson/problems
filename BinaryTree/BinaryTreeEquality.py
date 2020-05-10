from BinaryTree import *
"""Problem - Determine if two binary trees are equal"""


#Recursive function two check if two sub-trees (or trees if root node is provided) are equal
def is_equal(tree1, tree2):
    #Check if there are any signs of inquality
    if tree1 is None or tree2 is None or tree1.get_data() != tree2.get_data():
        #If both nodes are None, then the nodes are equal
        if tree1 is None and tree2 is None:
            return True
        return False

    tree_1_left = tree1.get_left()
    tree_2_left = tree2.get_left()
    tree_1_right = tree1.get_right()
    tree_2_right = tree2.get_right()

    #Check if the left subtrees are equal and if the right subtrees are equal
    if is_equal(tree_1_left, tree_2_left) and is_equal(tree_1_right, tree_2_right):
        return True

    return False

tree1 = BinaryTree()
tree1.insert(10)
tree1.insert(8)
tree1.insert(15)
tree1.insert(14)
tree1.print()
tree2 = BinaryTree()
tree2.insert(10)
tree2.insert(8)
tree2.insert(15)
tree2.insert(14)
tree2.print()

print("Are these binary trees equal?",is_equal(tree1.get_root(), tree2.get_root()))

tree1 = BinaryTree()
tree1.insert(10)
tree1.insert(8)
tree1.insert(15)
tree1.insert(14)
tree1.print()
tree2 = BinaryTree()
tree2.insert(10)
tree2.insert(8)
tree2.insert(1)
tree2.insert(14)
tree2.print()

print(is_equal(tree1.get_root(), tree2.get_root()))
print("Are these binary trees equal?",is_equal(tree1.get_root(), tree2.get_root()))
