# binary-trees
an implementation of binary trees

A tree is a data structure of nodes connected by edges. Binary tree is a special tree structure which can have at most 2 edges on each node.

Node: Node is the called to the elements of the tree.
Root: The top node is the root.
Child: The nodes connected to an upward node is called child nodes.
Leaf: Nodes that don't have any child.
Traversing: Following a spesific path in the tree.
Data: Value of the node.
Levels: Generations of nodes from parents to children. Level 0 (Root) to Level n.

Binary Search Tree Traverse Types:
In-Order: Searching the tree starting with the left sub-tree to root and finally right sub-tree.
Pre-Order: Visit the root first, then left sub-tree and right-subtree.
Post-order: Visit left and right sub-tree first, then root.

My class Node code is:

Node
  init
  insert
  print_node
  print_in_order
  print_pre_order
  print_post_order
  contains
