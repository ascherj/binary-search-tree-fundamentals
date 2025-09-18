class TreeNode:
    """
    A node in a Binary Search Tree.

    Attributes:
        val: The value stored in the node
        left: Reference to the left child node
        right: Reference to the right child node
    """
    def __init__(self, val: int) -> None:
        """
        Initialize a new tree node.

        Args:
            val: The value to store in the node
        """
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return f"TreeNode({self.val})"