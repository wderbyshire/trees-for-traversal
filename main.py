from binary_tree import BinTree

# Input data for the tree
input_data = [17, 8, 4, 12, 22, 19, 14, 5, 30, 25]

# Instantiate binary tree
new_tree = BinTree()

# Add all input values into the binary tree
for value in input_data:
    new_tree.add_node(value)

# Examples of searching through the binary tree
print(new_tree.search_value(21))
print(new_tree.search_value(22))

# Test code to run traversal algorithms you will develop
new_tree.in_order(new_tree.root)
new_tree.pre_order(new_tree.root)
new_tree.post_order(new_tree.root)
