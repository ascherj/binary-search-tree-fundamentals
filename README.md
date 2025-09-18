# Binary Search Tree Fundamentals

Comprehensive implementation and demonstration of Binary Search Tree concepts, including tree operations, traversal methods, and practical applications.

## Overview

This repository provides hands-on code examples covering core BST concepts:

### Tree Operations
- **Insert**: Add new nodes while maintaining BST property
- **Remove**: Delete nodes with three case handling (leaf, one child, two children)
- **Search**: Efficiently find values using BST properties

### Traversal Methods
- **In-order**: Left → Root → Right (produces sorted output for BST)
- **Pre-order**: Root → Left → Right (good for copying tree structure)
- **Post-order**: Left → Right → Root (good for deleting nodes)
- **Level-order**: Breadth-first traversal using a queue

### Utilities
- Tree visualization with ASCII art
- Tree statistics (height, node count)
- Demo tree builders

## Quick Start

### Basic Demo
```bash
python demos/basic_demo.py
```
Shows all traversal methods on a sample binary search tree.

### Educational Demo
```bash
python demos/educational_demo.py
```
Replicates original demo functionality with educational features:
- Step-by-step traversal explanations
- Multiple visualization formats
- Original vs enhanced comparisons

### Interactive Demo
```bash
python demos/interactive_demo.py
```
Comprehensive demonstration with:
- Multiple tree structures (simple, balanced, unbalanced)
- BST operations and search path tracking
- Tree statistics and comparisons
- Interactive tree building from value lists

## Example Output

### Tree Structure
```
       13
   6       21
 4   8   15   24
              26
```

### Traversal Results
```
In-order:    [4, 6, 8, 13, 15, 21, 24, 26]
Pre-order:   [13, 6, 4, 8, 21, 15, 24, 26]
Post-order:  [4, 8, 6, 15, 26, 24, 21, 13]
Level-order: [13, 6, 21, 4, 8, 15, 24, 26]
```

### BST Search Demo
```
Search 15: ✓ Path: 13 → 21 → 15
Search 25: ✗ Path: 13 → 21 → 24 → 26
```

## Project Structure

```
binary-search-tree-fundamentals/
├── tree_node.py           # TreeNode class definition
├── bst_operations.py      # Insert, remove, search operations
├── traversal_methods.py   # All traversal algorithms
├── tree_utilities.py      # Visualization and helper functions
├── demos/
│   ├── basic_demo.py      # Core functionality demonstration
│   ├── educational_demo.py # Original demo style + educational features
│   └── interactive_demo.py # Comprehensive tree comparisons
└── README.md
```

## Core Modules

### `tree_node.py`
- TreeNode class with type annotations
- String representations for debugging

### `bst_operations.py`
- `insert(root, val)` - Add nodes maintaining BST property
- `remove(root, val)` - Delete with three-case handling
- `search(root, target)` - Efficient value lookup
- `minValueNode(root)` - Find minimum value (helper for deletion)

### `traversal_methods.py`
- `inorder_traversal(root)` - Returns sorted sequence for BST
- `preorder_traversal(root)` - Root-first traversal
- `postorder_traversal(root)` - Root-last traversal
- `levelorder_traversal(root)` - Breadth-first using queue

### `tree_utilities.py`
- `print_tree(root)` - ASCII art visualization
- `print_tree_structure(root)` - Level-format visualization
- `show_inorder_steps(root)` - Step-by-step traversal explanation
- `build_demo_tree()` - Sample tree constructor
- `build_tree_from_values(values)` - Build BST from list
- `get_tree_height(root)` - Calculate tree height
- `count_nodes(root)` - Count total nodes

## Time Complexities

| Operation | Average | Worst Case |
|-----------|---------|------------|
| Search    | O(log n) | O(n) |
| Insert    | O(log n) | O(n) |
| Remove    | O(log n) | O(n) |
| Traversals| O(n)     | O(n) |

**Note:** Worst case occurs with unbalanced trees (essentially linked lists)

## Educational Use

This implementation helps students:
1. **Understand BST properties** - left < root < right
2. **Master traversal algorithms** - recursive and iterative approaches
3. **Practice tree operations** - insertion, deletion, search
4. **Visualize tree structures** - ASCII art representation
5. **Analyze complexity** - time/space tradeoffs
6. **Handle edge cases** - empty trees, single nodes, deletion scenarios

## Key Insights

- **In-order traversal** of BST produces sorted sequence
- **BST search** efficiently eliminates half the tree at each step
- **Tree balance** dramatically affects performance
- **Deletion cases** require careful handling of node relationships
- **Recursive solutions** naturally match tree structure

Perfect for computer science students preparing for technical interviews and algorithm assessments!
