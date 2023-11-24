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
    
    # Print the nodes
    print(f"root of the tree is {root.key}")
    for node in nodes_dict.values():
        print(f"Node {node.key} with children: {[child.key for child in node.children]}")
    
    return root, dic_r2

# Function to print the tree structure recursively with indentation
def print_tree(node, indent=0):
    if node:
        # Print the key of the current node with proper indentation
        print("  " * indent + f"Node {node.key}")
        # Recursively print the tree structure for each child with increased indentation
        for child in node.children:
            print_tree(child, indent + 1)

# Example usage:
parent_representation = [2, 7, 5, 2, 7, 7, -1, 5, 2, 8, 3, 9]

# Transformation T1
root, tree = transform_r1_to_r2(parent_representation)
# Print separators for clarity
print('#' * 50)
print('\n')
# Print the multi-way tree representation
print(tree)
print('\n')
# Print separators for clarity
print('#' * 50)
# Print the entire tree structure
print_tree(root)
