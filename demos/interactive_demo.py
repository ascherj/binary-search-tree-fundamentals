import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tree_node import TreeNode
from traversal_methods import inorder_traversal, preorder_traversal, postorder_traversal, levelorder_traversal
from tree_utilities import build_demo_tree, print_tree, build_tree_from_values, get_tree_height, count_nodes
from bst_operations import insert, search

class InteractiveTreeDemo:
    def __init__(self):
        pass

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
        return build_demo_tree()

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
                  \
                   5
        """
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        root.right.right.right.right = TreeNode(5)
        return root

    def demonstrate_tree(self, root, tree_name):
        """Demonstrate all traversals on a given tree"""
        print(f"\n{tree_name}")
        print("=" * len(tree_name))

        print("\nTree Structure:")
        print_tree(root)

        print(f"\nTree Stats: Height = {get_tree_height(root)}, Nodes = {count_nodes(root)}")

        print("\nTraversals:")
        print(f"  In-order:    {inorder_traversal(root)}")
        print(f"  Pre-order:   {preorder_traversal(root)}")
        print(f"  Post-order:  {postorder_traversal(root)}")
        print(f"  Level-order: {levelorder_traversal(root)}")

    def search_demo(self, root):
        """Demonstrate BST search with path tracking"""
        print("\nBST Search Demonstration:")
        print("-" * 30)

        test_values = [15, 7, 26, 1, 30]
        for target in test_values:
            path = []
            found = self.search_with_path(root, target, path)
            path_str = " → ".join(map(str, path)) if path else "empty"
            status = "✓ Found" if found else "✗ Not found"
            print(f"Search {target:2d}: {status:10s} Path: {path_str}")

    def search_with_path(self, root, target, path):
        """Search with path tracking for demonstration"""
        curr = root
        while curr:
            path.append(curr.val)
            if target == curr.val:
                return True
            elif target < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def comparison_demo(self):
        """Compare traversals across different tree structures"""
        trees = [
            (self.create_simple_tree(), "Simple 3-Node Tree"),
            (self.create_demo_tree(), "Balanced Demo Tree"),
            (self.create_unbalanced_tree(), "Unbalanced Tree")
        ]

        print("Tree Structure Comparison")
        print("=" * 50)

        for root, name in trees:
            self.demonstrate_tree(root, name)

        # Search demo on the balanced tree
        print("\n" + "=" * 50)
        self.search_demo(self.create_demo_tree())

    def interactive_builder_demo(self):
        """Demonstrate building a tree interactively"""
        print("\nInteractive Tree Builder Demo")
        print("=" * 40)

        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
        print(f"Building tree with values: {values}")

        root = build_tree_from_values(values)

        print("\nFinal Tree Structure:")
        print_tree(root)

        print(f"\nTree Properties:")
        print(f"  Height: {get_tree_height(root)}")
        print(f"  Total nodes: {count_nodes(root)}")
        print(f"  In-order traversal: {inorder_traversal(root)}")

        print("\nNote: In-order traversal of BST gives sorted sequence!")

def run_full_demo():
    """Run the complete interactive demo"""
    demo = InteractiveTreeDemo()

    print("Binary Search Tree Fundamentals - Interactive Demo")
    print("=" * 60)

    # Tree comparison
    demo.comparison_demo()

    # Interactive builder
    demo.interactive_builder_demo()

    print("\nDemo complete! 🌳")

if __name__ == "__main__":
    run_full_demo()