---

# Tree Transformation Toolkit

The Tree Transformation Toolkit is a Python library designed to simplify the conversion and visualization of tree structures. This toolkit provides a set of functions for transforming a tree from a parent representation to both multi-way and binary tree representations. Additionally, it includes visualization functions to print tree structures with proper indentation.

## Table of Contents

1. [Key Features](#key-features)
2. [Usage](#usage)
3. [Examples](#examples)


Make sure to check for any additional dependencies required by the toolkit.

## Key Features

1. **Transformation Functions:**
   - `transform_r1_to_r2(parent_representation)`: Converts a tree from a parent representation to a multi-way tree.
   - `multi_to_binary(multi_tree, current_key)`: Converts a multi-way tree to a binary tree.

2. **Visualization Functions:**
   - `print_tree_from_parent_representation(parent_representation)`: Prints the tree structure given its parent representation.
   - `print_tree(node, indent=0)`: Recursively prints the tree structure with proper indentation.
   - `print_binary_tree(node, level=0, prefix="Root: ")`: Prints the binary tree structure with proper indentation.

3. **Data Structures:**
   - `MultiWayTreeNode`: A class representing a node in a multi-way tree.
   - `BinaryNode`: A class representing a node in a binary tree.

## Usage

To incorporate the Tree Transformation Toolkit into your Python project, follow these steps:

1. Import the toolkit into your Python script or Jupyter notebook.
2. Use the provided functions according to your requirements.

Refer to the examples section for detailed usage scenarios.


## Examples

```python
from tree_transformation_toolkit import transform_r1_to_r2, multi_to_binary, print_tree, print_binary_tree, binary_tree_to_string

# Example usage
parent_representation = [2, 7, 5, 2, 7, 7, -1, 5, 2]
root, nodes = transform_r1_to_r2(parent_representation)
binary_tree_root = multi_to_binary(nodes, root.key)
output_string = binary_tree_to_string(binary_tree_root)

# Print multi-way tree
print_tree(root)

# Print binary tree structure
print_binary_tree(binary_tree_root)
```


---

