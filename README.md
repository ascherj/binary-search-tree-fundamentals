# Binary Tree Traversal Methods Demo

Interactive code demonstrations for learning Binary Tree Traversal methods.

## Overview

This repository provides hands-on code examples that demonstrate the four main binary tree traversal methods:

- **In-order**: Left → Root → Right (produces sorted output for BST)
- **Pre-order**: Root → Left → Right (good for copying tree structure)
- **Post-order**: Left → Right → Root (good for deleting nodes)
- **Level-order**: Breadth-first traversal using a queue

## Quick Start

### Basic Demo
```bash
python binary_tree_traversals.py
```
Shows all traversal methods on a sample binary search tree.

### Interactive Demo
```bash
python interactive_demo.py
```
Comprehensive demonstration with:
- Multiple tree structures (simple, balanced, unbalanced)
- Step-by-step traversal explanations
- BST search path visualization
- Side-by-side traversal comparisons

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

## Files

- `tree_node.py` - Basic TreeNode class
- `binary_tree_traversals.py` - Core traversal implementations and demos
- `interactive_demo.py` - Advanced interactive demonstrations

## Educational Use

This code is designed to help students:
1. Visualize how different traversals work
2. Understand when to use each traversal method
3. See step-by-step execution of algorithms
4. Practice with Binary Search Tree operations
5. Compare results across different tree structures

## Key Learning Points

- **In-order traversal** of a BST returns values in sorted order
- **Pre-order traversal** visits root first, useful for tree serialization
- **Post-order traversal** visits root last, useful for tree deletion
- **Level-order traversal** processes nodes level by level
- **BST search** efficiently eliminates half the tree at each step

Perfect for computer science students preparing for technical interviews and algorithm assessments!