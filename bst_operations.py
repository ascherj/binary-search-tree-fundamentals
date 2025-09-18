from tree_node import TreeNode

def insert(root: TreeNode | None, val: int) -> TreeNode:
    """
    Insert a new node into the BST and return the root.

    Args:
        root: The root node of the BST (can be None for empty tree)
        val: The value to insert

    Returns:
        TreeNode: The root node of the BST after insertion

    Time Complexity: O(log n) average, O(n) worst case (unbalanced tree)
    Space Complexity: O(log n) average, O(n) worst case (recursion stack)
    """
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

def minValueNode(root: TreeNode | None) -> TreeNode | None:
    """
    Find and return the node with the minimum value in the BST.

    Args:
        root: The root node of the BST or subtree

    Returns:
        TreeNode: The node containing the minimum value, or None if tree is empty

    Time Complexity: O(log n) average, O(n) worst case (unbalanced tree)
    Space Complexity: O(1) - iterative approach uses constant space
    """
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def remove(root: TreeNode | None, val: int) -> TreeNode | None:
    """
    Remove a node with the given value from the BST and return the root.

    Handles three deletion cases:
    1. Node with no children (leaf node)
    2. Node with one child
    3. Node with two children (uses inorder successor)

    Args:
        root: The root node of the BST (can be None for empty tree)
        val: The value to remove from the BST

    Returns:
        TreeNode: The root node of the BST after removal, or None if tree becomes empty

    Time Complexity: O(log n) average, O(n) worst case (unbalanced tree)
    Space Complexity: O(log n) average, O(n) worst case (recursion stack)
    """
    if not root:
        return None

    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        # Node to be deleted found - handle 3 cases:

        # Case 1: Node has no left child (0 or 1 child on right)
        if not root.left:
            return root.right
        # Case 2: Node has left child but no right child (1 child on left)
        elif not root.right:
            return root.left
        # Case 3: Node has both left and right children
        else:
            # Find the inorder successor (smallest value in right subtree)
            minNode = minValueNode(root.right)
            # Replace current node's value with successor's value
            root.val = minNode.val
            # Delete the successor from right subtree
            root.right = remove(root.right, minNode.val)
    return root

def search(root: TreeNode | None, target: int) -> bool:
    """
    Search for a target value in the BST.

    Args:
        root: The root node of the BST
        target: The value to search for

    Returns:
        bool: True if target is found, False otherwise

    Time Complexity: O(log n) average, O(n) worst case (unbalanced tree)
    Space Complexity: O(1) - iterative approach uses constant space
    """
    curr = root
    while curr:
        if target == curr.val:
            return True
        elif target < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    return False