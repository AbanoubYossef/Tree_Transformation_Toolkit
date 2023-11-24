# Define a class representing a node in a multi-way tree
class MultiWayTreeNode:
    def __init__(self, key):
        self.key = key
        self.children = []

# Function to transform a parent representation into a multi-way tree
def transform_r1_to_r2(parent_representation):
    # Create a dictionary to map parent indices to nodes
    nodes_dict = {i + 1: MultiWayTreeNode(i + 1) for i in range(len(parent_representation))}
    
    # Initialize the root node as None
    root = None

    # Iterate through the parent representation
    for child_index, parent_index in enumerate(parent_representation, start=1):
        # If the parent is -1, the current node is the root
        if parent_index == -1:
            root = nodes_dict[child_index]
        else:
            # Append the current node to its parent's list of children
            nodes_dict[parent_index].children.append(nodes_dict[child_index])
    
    # Create a dictionary to store the multi-way tree representation
    dic_r2 = {}
    # Update the dictionary with the root and its children
    dic_r2.update({root.key: [child.key for child in root.children]})
    # Iterate through the children of the root and update the dictionary recursively
    for node in dic_r2[root.key]:
        dic_r2.update({nodes_dict[node].key: [child.key for child in nodes_dict[node].children]})
    # Iterate through all nodes in the tree and update the dictionary
    for i in range(len(nodes_dict)):
        for nodes in list(dic_r2.values()):
            for node in nodes:
                if node:
                    dic_r2.update({nodes_dict[node].key: [child.key for child in nodes_dict[node].children]})
    
    return root, dic_r2

# Define a class representing a node in a binary tree
class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to convert a multi-way tree to a binary tree
def multi_to_binary(multi_tree, current_key):
    # Check if the current key is in the multi-way tree
    if current_key not in multi_tree:
        return None

    # Create a new binary tree node with the current key as data
    node = BinaryNode(current_key)
    # Get the children of the current key from the multi-way tree
    children = multi_tree[current_key]

    # If there are children, create the left child and add the rest as right children
    if children:
        # Create the left child and assign it to the current node's left attribute
        node.left = multi_to_binary(multi_tree, children[0])

        # For the rest of the children, add them to the right
        current_right = node.left
        for child in children[1:]:
            current_right.right = multi_to_binary(multi_tree, child)
            current_right = current_right.right

    return node

# Function to convert a binary tree to a string representation
def binary_tree_to_string(node):
    # Check if the node is None
    if node is None:
        return ""

    # Initialize the result with the data of the current node
    result = str(node.data)
    # Check if there are left or right children
    if node.left or node.right:
        result += "["
        # If there is a left child, recursively add its string representation
        if node.left:
            result += binary_tree_to_string(node.left)
        result += "]"
        # If there is a right child, recursively add its string representation
        if node.right:
            result += "["
            result += binary_tree_to_string(node.right)
            result += "]"

    return result

# Function to print the binary tree structure with proper indentation
def print_binary_tree(node, level=0, prefix="Root: "):
    # Check if the node is not None
    if node is not None:
        # Print the data of the current node with proper indentation and prefix
        print(" " * (level * 4) + prefix + str(node.data))
        # Check if there are left or right children
        if node.left or node.right:
            # If there is a left child, recursively print its structure with increased indentation and "L---" prefix
            if node.left:
                print_binary_tree(node.left, level + 1, "L--- ")
            # If there is a right child, recursively print its structure with increased indentation and "R---" prefix
            if node.right:
                print_binary_tree(node.right, level + 1, "R--- ")

# Example usage:
parent_representation = [2, 7, 5, 2, 7, 7, -1, 5, 2]
# Transformation T1
root, nodes = transform_r1_to_r2(parent_representation)
# Convert multi-way tree to binary tree
binary_tree_root = multi_to_binary(nodes, root.key)

# Convert binary tree to string
output_string = binary_tree_to_string(binary_tree_root)
print('\n')
print(output_string)
print('\n')
# Print separators for clarity
print('#' * 50)
print('\n')
# Print the binary tree using the fun visualization
print_binary_tree(binary_tree_root)
