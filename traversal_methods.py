from tree_node import TreeNode
from collections import deque

def inorder_traversal(root: TreeNode | None) -> list[int]:
    """
    In-order traversal: Left > Root > Right
    For BST, this returns values in sorted order

    Time Complexity: O(n) - visits each node once
    Space Complexity: O(h) where h is height (recursion stack)
    """
    result = []

    def inorder_helper(node):
        if node:
            inorder_helper(node.left)    # Visit left subtree
            result.append(node.val)      # Process root
            inorder_helper(node.right)   # Visit right subtree

    inorder_helper(root)
    return result

def preorder_traversal(root: TreeNode | None) -> list[int]:
    """
    Pre-order traversal: Root > Left > Right
    Good for copying/serializing tree structure

    Time Complexity: O(n) - visits each node once
    Space Complexity: O(h) where h is height (recursion stack)
    """
    result = []

    def preorder_helper(node):
        if node:
            result.append(node.val)      # Process root first
            preorder_helper(node.left)   # Visit left subtree
            preorder_helper(node.right)  # Visit right subtree

    preorder_helper(root)
    return result

def postorder_traversal(root: TreeNode | None) -> list[int]:
    """
    Post-order traversal: Left > Right > Root
    Good for deleting nodes or calculating size

    Time Complexity: O(n) - visits each node once
    Space Complexity: O(h) where h is height (recursion stack)
    """
    result = []

    def postorder_helper(node):
        if node:
            postorder_helper(node.left)  # Visit left subtree
            postorder_helper(node.right) # Visit right subtree
            result.append(node.val)      # Process root last

    postorder_helper(root)
    return result

def levelorder_traversal(root: TreeNode | None) -> list[int]:
    """
    Level-order traversal (breadth-first): Level by level
    Uses a queue to process nodes

    Time Complexity: O(n) - visits each node once
    Space Complexity: O(w) where w is max width of tree
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result