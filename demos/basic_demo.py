import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tree_node import TreeNode
from traversal_methods import inorder_traversal, preorder_traversal, postorder_traversal, levelorder_traversal
from tree_utilities import build_demo_tree, print_tree, print_tree_structure, show_inorder_steps
from bst_operations import search

def basic_traversal_demo():
    """
    Demonstrate all traversal methods with the sample tree
    """
    print("Binary Search Tree Fundamentals - Basic Demo")
    print("=" * 50)

    # Build the demo tree
    root = build_demo_tree()

    # Show tree structure (ASCII art)
    print("Tree Structure (ASCII):")
    print_tree(root)
    print()

    # Show tree structure (level format)
    print("Tree Structure (Level format):")
    print_tree_structure(root)
    print()

    # Demonstrate all traversals
    print("Traversal Results:")
    print("-" * 30)

    inorder = inorder_traversal(root)
    print(f"In-order (Left > Root > Right):   {inorder}")

    preorder = preorder_traversal(root)
    print(f"Pre-order (Root > Left > Right):  {preorder}")

    postorder = postorder_traversal(root)
    print(f"Post-order (Left > Right > Root): {postorder}")

    levelorder = levelorder_traversal(root)
    print(f"Level-order (Breadth-first):      {levelorder}")
    print()

    # Show step-by-step in-order traversal
    print("In-order Traversal Step-by-Step:")
    print("-" * 35)
    show_inorder_steps(root)
    print()

    # Demonstrate BST search
    print("BST Search Demo:")
    print("-" * 20)
    test_values = [15, 7, 26, 30]
    for val in test_values:
        found = search(root, val)
        print(f"Searching for {val}: {'Found' if found else 'Not found'}")

if __name__ == "__main__":
    basic_traversal_demo()