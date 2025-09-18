import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tree_node import TreeNode
from traversal_methods import inorder_traversal, preorder_traversal, postorder_traversal, levelorder_traversal
from tree_utilities import build_demo_tree, print_tree, print_tree_structure, show_inorder_steps
from bst_operations import search

def original_demo_style():
    """
    Replicate the exact functionality from binary_tree_traversals.py demo_all_traversals()
    """
    print("Binary Tree Traversal Demo")
    print("=" * 50)

    # Build the demo tree
    root = build_demo_tree()

    # Show tree structure
    print("Tree Structure:")
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

    # Demonstrate BST search
    print("BST Search Demo:")
    print("-" * 20)
    test_values = [15, 7, 26, 30]
    for val in test_values:
        found = search(root, val)
        print(f"Searching for {val}: {'Found' if found else 'Not found'}")

def educational_features_demo():
    """
    Show educational features like step-by-step traversal
    """
    print("\n" + "=" * 50)
    print("Educational Features Demo")
    print("=" * 50)

    root = build_demo_tree()

    print("Step-by-step In-order Traversal:")
    print("-" * 35)
    show_inorder_steps(root)
    print()

    print("Tree Visualization Comparison:")
    print("-" * 30)
    print("ASCII Tree Format:")
    print_tree(root)
    print("\nLevel Format:")
    print_tree_structure(root)

if __name__ == "__main__":
    original_demo_style()
    educational_features_demo()