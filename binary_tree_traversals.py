from tree_node import TreeNode
from collections import deque

class BinaryTreeTraversals:
    
    def inorder_traversal(self, root):
        """
        In-order traversal: Left > Root > Right
        For BST, this returns values in sorted order
        """
        result = []
        
        def inorder_helper(node):
            if node:
                inorder_helper(node.left)    # Visit left subtree
                result.append(node.val)      # Process root
                inorder_helper(node.right)   # Visit right subtree
        
        inorder_helper(root)
        return result
    
    def preorder_traversal(self, root):
        """
        Pre-order traversal: Root > Left > Right
        Good for copying/serializing tree structure
        """
        result = []
        
        def preorder_helper(node):
            if node:
                result.append(node.val)      # Process root first
                preorder_helper(node.left)   # Visit left subtree
                preorder_helper(node.right)  # Visit right subtree
        
        preorder_helper(root)
        return result
    
    def postorder_traversal(self, root):
        """
        Post-order traversal: Left > Right > Root
        Good for deleting nodes or calculating size
        """
        result = []
        
        def postorder_helper(node):
            if node:
                postorder_helper(node.left)  # Visit left subtree
                postorder_helper(node.right) # Visit right subtree
                result.append(node.val)      # Process root last
        
        postorder_helper(root)
        return result
    
    def levelorder_traversal(self, root):
        """
        Level-order traversal (breadth-first): Level by level
        Uses a queue to process nodes
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
    
    def search_bst(self, root, target):
        """
        Search for a value in a Binary Search Tree
        Returns True if found, False otherwise
        """
        if not root:
            return False
        
        if target == root.val:
            return True
        elif target < root.val:
            return self.search_bst(root.left, target)
        else:
            return self.search_bst(root.right, target)
    
    def build_demo_tree(self):
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
    
    def print_tree_structure(self, root):
        """
        Print tree structure in traditional top-down format
        """
        if not root:
            print("Empty tree")
            return
        
        def get_tree_height(node):
            if not node:
                return 0
            return 1 + max(get_tree_height(node.left), get_tree_height(node.right))
        
        def print_level(nodes, level, max_level):
            if not nodes or all(node is None for node in nodes):
                return
            
            floor = max_level - level
            edge_lines = 2 ** max(floor - 1, 0)
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
    
    def demo_all_traversals(self):
        """
        Demonstrate all traversal methods with the sample tree
        """
        print("Binary Tree Traversal Demo")
        print("=" * 50)
        
        # Build the demo tree
        root = self.build_demo_tree()
        
        # Show tree structure
        print("Tree Structure:")
        self.print_tree_structure(root)
        print()
        
        # Demonstrate all traversals
        print("Traversal Results:")
        print("-" * 30)
        
        inorder = self.inorder_traversal(root)
        print(f"In-order (Left > Root > Right):   {inorder}")
        
        preorder = self.preorder_traversal(root)
        print(f"Pre-order (Root > Left > Right):  {preorder}")
        
        postorder = self.postorder_traversal(root)
        print(f"Post-order (Left > Right > Root): {postorder}")
        
        levelorder = self.levelorder_traversal(root)
        print(f"Level-order (Breadth-first):      {levelorder}")
        print()
        
        # Demonstrate BST search
        print("BST Search Demo:")
        print("-" * 20)
        test_values = [15, 7, 26, 30]
        for val in test_values:
            found = self.search_bst(root, val)
            print(f"Searching for {val}: {'Found' if found else 'Not found'}")

if __name__ == "__main__":
    demo = BinaryTreeTraversals()
    demo.demo_all_traversals()