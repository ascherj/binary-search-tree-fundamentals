from tree_node import TreeNode
from bst_operations import insert

def print_tree(root: TreeNode | None, prefix: str = "", is_last: bool = True, is_root: bool = True) -> None:
    """
    Print a visual representation of the BST using ASCII art.

    Args:
        root: The root node of the tree or subtree to print
        prefix: String prefix for indentation (used internally for recursion)
        is_last: Whether this node is the last child (used internally for recursion)
        is_root: Whether this is the root node (used internally for recursion)

    Time Complexity: O(n) - visits each node once
    Space Complexity: O(h) where h is height (recursion stack)
    """
    if not root:
        return

    if is_root:
        print(f"{root.val}")
    else:
        connector = "└── " if is_last else "├── "
        print(prefix + connector + str(root.val))

    children = []
    if root.right:
        children.append((root.right, False))
    if root.left:
        children.append((root.left, True))

    for i, (child, is_left) in enumerate(children):
        is_last_child = (i == len(children) - 1)
        if is_root:
            extension = "    "
        else:
            extension = "│   " if not is_last else "    "
        print_tree(child, prefix + extension, is_last_child, False)

def build_demo_tree() -> TreeNode:
    """
    Build a sample binary search tree for demonstration:
          13
        /    \
       6      21
      / \    /  \
     4   8  15  24
                 \
                 26
    """
    root = TreeNode(13)
    root.left = TreeNode(6)
    root.right = TreeNode(21)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(8)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(24)

    root.right.right.right = TreeNode(26)

    return root

def build_tree_from_values(values: list[int]) -> TreeNode | None:
    """
    Build a BST from a list of values using the insert operation.

    Args:
        values: List of integers to insert into the BST

    Returns:
        TreeNode: Root of the constructed BST, or None if values is empty
    """
    if not values:
        return None

    root = None
    for val in values:
        root = insert(root, val)
    return root

def get_tree_height(root: TreeNode | None) -> int:
    """
    Calculate the height of the tree.

    Args:
        root: The root node of the tree

    Returns:
        int: The height of the tree (0 for empty tree, 1 for single node)
    """
    if not root:
        return 0
    return 1 + max(get_tree_height(root.left), get_tree_height(root.right))

def count_nodes(root: TreeNode | None) -> int:
    """
    Count the total number of nodes in the tree.

    Args:
        root: The root node of the tree

    Returns:
        int: The total number of nodes
    """
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def print_tree_structure(root: TreeNode | None) -> None:
    """
    Print tree structure in traditional top-down level format.
    Alternative visualization to print_tree() ASCII art.

    Args:
        root: The root node of the tree to print
    """
    if not root:
        print("Empty tree")
        return

    def print_level(nodes, level, max_level):
        if not nodes or all(node is None for node in nodes):
            return

        floor = max_level - level
        first_spaces = 2 ** floor - 1
        between_spaces = 2 ** (floor + 1) - 1

        print(" " * first_spaces, end="")

        new_nodes = []
        for i, node in enumerate(nodes):
            if node:
                print(node.val, end="")
                new_nodes.extend([node.left, node.right])
            else:
                print(" ", end="")
                new_nodes.extend([None, None])

            if i < len(nodes) - 1:
                print(" " * between_spaces, end="")

        print()

        if level < max_level:
            print_level(new_nodes, level + 1, max_level)

    height = get_tree_height(root)
    print_level([root], 1, height)

def show_inorder_steps(root: TreeNode | None, depth: int = 0) -> None:
    """
    Show step-by-step in-order traversal for educational purposes.

    Args:
        root: The root node of the tree or subtree
        depth: Current recursion depth (for indentation)
    """
    if root:
        indent = "  " * depth
        print(f"{indent}Visit node {root.val}")
        if root.left:
            print(f"{indent}Go left from {root.val}")
            show_inorder_steps(root.left, depth + 1)
        print(f"{indent}Process {root.val}")
        if root.right:
            print(f"{indent}Go right from {root.val}")
            show_inorder_steps(root.right, depth + 1)