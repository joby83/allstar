"""
Red-Black Tree Implementation

A Red-Black Tree is a self-balancing binary search tree with the following properties:
1. Every node is either red or black
2. The root is black
3. All leaves (NIL) are black
4. If a node is red, then both its children are black
5. Every path from a node to its descendant NIL nodes has the same number of black nodes
"""

class Color:
    RED = 0
    BLACK = 1


class Node:
    def __init__(self, key, value=None, color=Color.RED):
        self.key = key
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        color_str = "R" if self.color == Color.RED else "B"
        return f"Node({self.key}, {color_str})"


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(key=None, color=Color.BLACK)
        self.root = self.NIL

    def insert(self, key, value=None):
        """Insert a new node with the given key and value."""
        new_node = Node(key, value, Color.RED)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        # Find the position to insert
        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            elif new_node.key > current.key:
                current = current.right
            else:
                # Key already exists, update value
                current.value = value
                return

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix Red-Black Tree properties
        self._fix_insert(new_node)

    def _fix_insert(self, node):
        """Fix Red-Black Tree properties after insertion."""
        while node.parent and node.parent.color == Color.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == Color.RED:
                    # Case 1: Uncle is red
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Case 2: Node is right child
                        node = node.parent
                        self._left_rotate(node)
                    # Case 3: Node is left child
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == Color.RED:
                    # Case 1: Uncle is red
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Case 2: Node is left child
                        node = node.parent
                        self._right_rotate(node)
                    # Case 3: Node is right child
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._left_rotate(node.parent.parent)

        self.root.color = Color.BLACK

    def delete(self, key):
        """Delete a node with the given key."""
        node = self._search_node(self.root, key)
        if node == self.NIL:
            return False

        self._delete_node(node)
        return True

    def _delete_node(self, node):
        """Delete the given node from the tree."""
        original_color = node.color

        if node.left == self.NIL:
            replacement = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL:
            replacement = node.left
            self._transplant(node, node.left)
        else:
            # Node has two children
            successor = self._minimum(node.right)
            original_color = successor.color
            replacement = successor.right

            if successor.parent == node:
                replacement.parent = successor
            else:
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor

            self._transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor
            successor.color = node.color

        if original_color == Color.BLACK:
            self._fix_delete(replacement)

    def _fix_delete(self, node):
        """Fix Red-Black Tree properties after deletion."""
        while node != self.root and node.color == Color.BLACK:
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == Color.RED:
                    # Case 1: Sibling is red
                    sibling.color = Color.BLACK
                    node.parent.color = Color.RED
                    self._left_rotate(node.parent)
                    sibling = node.parent.right

                if sibling.left.color == Color.BLACK and sibling.right.color == Color.BLACK:
                    # Case 2: Sibling's children are both black
                    sibling.color = Color.RED
                    node = node.parent
                else:
                    if sibling.right.color == Color.BLACK:
                        # Case 3: Sibling's right child is black
                        sibling.left.color = Color.BLACK
                        sibling.color = Color.RED
                        self._right_rotate(sibling)
                        sibling = node.parent.right

                    # Case 4: Sibling's right child is red
                    sibling.color = node.parent.color
                    node.parent.color = Color.BLACK
                    sibling.right.color = Color.BLACK
                    self._left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == Color.RED:
                    # Case 1: Sibling is red
                    sibling.color = Color.BLACK
                    node.parent.color = Color.RED
                    self._right_rotate(node.parent)
                    sibling = node.parent.left

                if sibling.right.color == Color.BLACK and sibling.left.color == Color.BLACK:
                    # Case 2: Sibling's children are both black
                    sibling.color = Color.RED
                    node = node.parent
                else:
                    if sibling.left.color == Color.BLACK:
                        # Case 3: Sibling's left child is black
                        sibling.right.color = Color.BLACK
                        sibling.color = Color.RED
                        self._left_rotate(sibling)
                        sibling = node.parent.left

                    # Case 4: Sibling's left child is red
                    sibling.color = node.parent.color
                    node.parent.color = Color.BLACK
                    sibling.left.color = Color.BLACK
                    self._right_rotate(node.parent)
                    node = self.root

        node.color = Color.BLACK

    def search(self, key):
        """Search for a node with the given key."""
        node = self._search_node(self.root, key)
        if node == self.NIL:
            return None
        return node.value

    def _search_node(self, node, key):
        """Helper method to search for a node."""
        if node == self.NIL or key == node.key:
            return node

        if key < node.key:
            return self._search_node(node.left, key)
        return self._search_node(node.right, key)

    def _left_rotate(self, node):
        """Perform left rotation."""
        right_child = node.right
        node.right = right_child.left

        if right_child.left != self.NIL:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def _right_rotate(self, node):
        """Perform right rotation."""
        left_child = node.left
        node.left = left_child.right

        if left_child.right != self.NIL:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child

    def _transplant(self, u, v):
        """Replace subtree rooted at u with subtree rooted at v."""
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node):
        """Find the minimum node in the subtree."""
        while node.left != self.NIL:
            node = node.left
        return node

    def _maximum(self, node):
        """Find the maximum node in the subtree."""
        while node.right != self.NIL:
            node = node.right
        return node

    def inorder_traversal(self):
        """Return inorder traversal of the tree."""
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node, result):
        """Helper method for inorder traversal."""
        if node != self.NIL:
            self._inorder_helper(node.left, result)
            result.append((node.key, node.value))
            self._inorder_helper(node.right, result)

    def preorder_traversal(self):
        """Return preorder traversal of the tree."""
        result = []
        self._preorder_helper(self.root, result)
        return result

    def _preorder_helper(self, node, result):
        """Helper method for preorder traversal."""
        if node != self.NIL:
            result.append((node.key, node.value))
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)

    def get_height(self):
        """Get the height of the tree."""
        return self._height_helper(self.root)

    def _height_helper(self, node):
        """Helper method to calculate height."""
        if node == self.NIL:
            return 0
        return 1 + max(self._height_helper(node.left), self._height_helper(node.right))

    def is_empty(self):
        """Check if the tree is empty."""
        return self.root == self.NIL

    def __len__(self):
        """Return the number of nodes in the tree."""
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        """Helper method to count nodes."""
        if node == self.NIL:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def __contains__(self, key):
        """Check if key exists in the tree."""
        return self.search(key) is not None

    def __repr__(self):
        """String representation of the tree."""
        if self.is_empty():
            return "RedBlackTree(empty)"
        return f"RedBlackTree(size={len(self)}, height={self.get_height()})"
