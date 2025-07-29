from binary_tree_traversals import BinaryTreeTraversals, TreeNode

class InteractiveTreeDemo:
    def __init__(self):
        self.traversals = BinaryTreeTraversals()
    
    def create_simple_tree(self):
        """
        Create a simple 3-node tree:
           2
          / \
         1   3
        """
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        return root
    
    def create_demo_tree(self):
        """Create the main demo tree"""
        return self.traversals.build_demo_tree()
    
    def create_unbalanced_tree(self):
        """
        Create an unbalanced tree:
           1
            \
             2
              \
               3
                \
                 4
        """
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        return root
    
    def compare_traversals(self, tree_name, root):
        """Compare all traversals for a given tree"""
        print(f"\n{tree_name}")
        print("=" * len(tree_name))
        
        print("\nTree Structure:")
        self.traversals.print_tree_structure(root)
        
        print(f"\nTraversal Comparisons:")
        print("-" * 25)
        
        inorder = self.traversals.inorder_traversal(root)
        preorder = self.traversals.preorder_traversal(root)
        postorder = self.traversals.postorder_traversal(root)
        levelorder = self.traversals.levelorder_traversal(root)
        
        print(f"In-order:    {inorder}")
        print(f"Pre-order:   {preorder}")
        print(f"Post-order:  {postorder}")
        print(f"Level-order: {levelorder}")
        
        # Show step-by-step for in-order
        print(f"\nIn-order step-by-step:")
        self.show_inorder_steps(root)
    
    def show_inorder_steps(self, root, depth=0):
        """Show step-by-step in-order traversal"""
        if root:
            indent = "  " * depth
            print(f"{indent}Visit node {root.val}")
            if root.left:
                print(f"{indent}Go left from {root.val}")
                self.show_inorder_steps(root.left, depth + 1)
            print(f"{indent}Process {root.val}")
            if root.right:
                print(f"{indent}Go right from {root.val}")
                self.show_inorder_steps(root.right, depth + 1)
    
    def run_demo(self):
        """Run interactive demo with different tree types"""
        print("Binary Tree Traversal Interactive Demo")
        print("=" * 40)
        
        # Demo 1: Simple tree
        simple_tree = self.create_simple_tree()
        self.compare_traversals("Simple Tree Demo", simple_tree)
        
        # Demo 2: Main demo tree
        demo_tree = self.create_demo_tree()
        self.compare_traversals("Main Demo Tree", demo_tree)
        
        # Demo 3: Unbalanced tree
        unbalanced_tree = self.create_unbalanced_tree()
        self.compare_traversals("Unbalanced Tree Demo", unbalanced_tree)
        
        # Search demo
        print("\n" + "=" * 40)
        print("Binary Search Tree Search Demo")
        print("=" * 40)
        
        print("\nSearching in the demo tree (BST):")
        test_values = [4, 13, 15, 25, 26]
        for val in test_values:
            path = self.get_search_path(demo_tree, val)
            found = self.traversals.search_bst(demo_tree, val)
            status = "✓" if found else "✗"
            print(f"Search {val}: {status} Path: {' → '.join(map(str, path))}")
    
    def get_search_path(self, root, target):
        """Get the path taken during BST search"""
        path = []
        current = root
        
        while current:
            path.append(current.val)
            if target == current.val:
                break
            elif target < current.val:
                current = current.left
            else:
                current = current.right
        
        return path

if __name__ == "__main__":
    demo = InteractiveTreeDemo()
    demo.run_demo()