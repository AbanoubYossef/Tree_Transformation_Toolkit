####################################################################################
# Function to print a tree structure given its parent representation
def print_tree_from_parent_representation(parent_representation):
    # Create a dictionary to store child nodes for each parent
    nodes_dict = {i: [] for i in range(1, len(parent_representation) + 1)}
    # Variable to store the root of the tree
    root = None

    # Loop through the parent representation to populate nodes_dict and find the root
    for child_index, parent_index in enumerate(parent_representation):
        # If parent_index is -1, it means the current node is the root
        if parent_index == -1:
            root = child_index + 1
        else:
            # Add the child node to the list of children for the parent node
            nodes_dict[parent_index].append(child_index + 1)

    # Recursive function to print the tree structure
    def print_recursive(node, indent=0):
        # Check if the current node has children
        if node in nodes_dict:
            # Print the current node
            print("  " * indent + f"Node {node}")
            # Recursively call the function for each child node
            for child in nodes_dict[node]:
                print_recursive(child, indent + 1)

    # Start printing the tree structure from the root
    print_recursive(root)

# Example usage:
# Define a parent representation for the tree
parent_representation = [2, 7, 5, 2, 7, 7, -1, 5, 2]
# Call the function to print the tree structure
print_tree_from_parent_representation(parent_representation)
#####################################################################################
