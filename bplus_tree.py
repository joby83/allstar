"""
B+ Tree Implementation

A B+ Tree is a self-balancing tree data structure commonly used in databases and file systems.
Key properties:
1. All values are stored in leaf nodes
2. Internal nodes only store keys for navigation
3. Leaf nodes are linked together for efficient range queries
4. All leaf nodes are at the same level
5. Each node (except root) has between ceil(order/2) and order children
"""

import math


class Node:
    def __init__(self, order, is_leaf=False):
        self.order = order
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []
        self.next = None  # For linking leaf nodes

    def is_full(self):
        """Check if node is full."""
        return len(self.keys) >= self.order - 1

    def is_underflow(self):
        """Check if node has too few keys."""
        min_keys = math.ceil(self.order / 2) - 1
        return len(self.keys) < min_keys

    def __repr__(self):
        return f"Node(keys={self.keys}, is_leaf={self.is_leaf})"


class LeafNode(Node):
    def __init__(self, order):
        super().__init__(order, is_leaf=True)
        self.values = []  # Store values corresponding to keys

    def insert(self, key, value):
        """Insert key-value pair into leaf node."""
        if not self.keys:
            self.keys.append(key)
            self.values.append(value)
            return

        # Find insertion position
        i = 0
        while i < len(self.keys) and self.keys[i] < key:
            i += 1

        # Update value if key exists
        if i < len(self.keys) and self.keys[i] == key:
            self.values[i] = value
            return

        # Insert key and value
        self.keys.insert(i, key)
        self.values.insert(i, value)

    def split(self):
        """Split leaf node when full."""
        mid = len(self.keys) // 2
        new_leaf = LeafNode(self.order)

        new_leaf.keys = self.keys[mid:]
        new_leaf.values = self.values[mid:]
        new_leaf.next = self.next

        self.keys = self.keys[:mid]
        self.values = self.values[:mid]
        self.next = new_leaf

        return new_leaf.keys[0], new_leaf

    def __repr__(self):
        return f"LeafNode(keys={self.keys}, values={self.values})"


class InternalNode(Node):
    def __init__(self, order):
        super().__init__(order, is_leaf=False)

    def insert_child(self, key, child):
        """Insert a child pointer at the appropriate position."""
        i = 0
        while i < len(self.keys) and self.keys[i] < key:
            i += 1

        self.keys.insert(i, key)
        self.children.insert(i + 1, child)

    def split(self):
        """Split internal node when full."""
        mid = len(self.keys) // 2
        split_key = self.keys[mid]
        new_internal = InternalNode(self.order)

        new_internal.keys = self.keys[mid + 1:]
        new_internal.children = self.children[mid + 1:]

        self.keys = self.keys[:mid]
        self.children = self.children[:mid + 1]

        return split_key, new_internal

    def __repr__(self):
        return f"InternalNode(keys={self.keys}, num_children={len(self.children)})"


class BPlusTree:
    def __init__(self, order=4):
        """
        Initialize B+ Tree with given order.
        Order is the maximum number of children a node can have.
        """
        if order < 3:
            raise ValueError("Order must be at least 3")
        self.order = order
        self.root = LeafNode(order)
        self.leftmost_leaf = self.root

    def insert(self, key, value):
        """Insert a key-value pair into the B+ Tree."""
        # Find the leaf node where key should be inserted
        leaf = self._find_leaf(key)
        leaf.insert(key, value)

        # Split if necessary
        if leaf.is_full():
            self._split_leaf(leaf, key)

    def _find_leaf(self, key):
        """Find the leaf node where key should be inserted/found."""
        node = self.root

        while not node.is_leaf:
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            node = node.children[i]

        return node

    def _split_leaf(self, leaf, key):
        """Split a full leaf node and propagate splits up the tree."""
        split_key, new_leaf = leaf.split()

        # If root is a leaf, create new root
        if leaf == self.root:
            new_root = InternalNode(self.order)
            new_root.keys = [split_key]
            new_root.children = [leaf, new_leaf]
            self.root = new_root
            return

        # Find parent and insert split key
        parent = self._find_parent(self.root, leaf)
        parent.insert_child(split_key, new_leaf)

        # Split parent if necessary
        if parent.is_full():
            self._split_internal(parent)

    def _split_internal(self, internal_node):
        """Split a full internal node and propagate splits up the tree."""
        split_key, new_internal = internal_node.split()

        # If splitting root, create new root
        if internal_node == self.root:
            new_root = InternalNode(self.order)
            new_root.keys = [split_key]
            new_root.children = [internal_node, new_internal]
            self.root = new_root
            return

        # Find parent and insert split key
        parent = self._find_parent(self.root, internal_node)
        parent.insert_child(split_key, new_internal)

        # Recursively split parent if necessary
        if parent.is_full():
            self._split_internal(parent)

    def _find_parent(self, current, target):
        """Find the parent node of target node."""
        if current.is_leaf:
            return None

        for child in current.children:
            if child == target:
                return current

        for i, child in enumerate(current.children):
            if not child.is_leaf:
                result = self._find_parent(child, target)
                if result:
                    return result

        return None

    def search(self, key):
        """Search for a key and return its value."""
        leaf = self._find_leaf(key)

        for i, k in enumerate(leaf.keys):
            if k == key:
                return leaf.values[i]

        return None

    def delete(self, key):
        """Delete a key from the B+ Tree."""
        leaf = self._find_leaf(key)

        # Find and remove key from leaf
        if key not in leaf.keys:
            return False

        idx = leaf.keys.index(key)
        leaf.keys.pop(idx)
        leaf.values.pop(idx)

        # Handle underflow if necessary
        if leaf != self.root and leaf.is_underflow():
            self._handle_underflow(leaf)

        return True

    def _handle_underflow(self, node):
        """Handle underflow in a node by borrowing or merging."""
        parent = self._find_parent(self.root, node)
        if not parent:
            return

        # Find node's index in parent
        node_idx = parent.children.index(node)

        # Try to borrow from left sibling
        if node_idx > 0:
            left_sibling = parent.children[node_idx - 1]
            if len(left_sibling.keys) > math.ceil(self.order / 2) - 1:
                self._borrow_from_left(node, left_sibling, parent, node_idx)
                return

        # Try to borrow from right sibling
        if node_idx < len(parent.children) - 1:
            right_sibling = parent.children[node_idx + 1]
            if len(right_sibling.keys) > math.ceil(self.order / 2) - 1:
                self._borrow_from_right(node, right_sibling, parent, node_idx)
                return

        # Merge with sibling
        if node_idx > 0:
            self._merge_with_left(node, parent, node_idx)
        else:
            self._merge_with_right(node, parent, node_idx)

    def _borrow_from_left(self, node, left_sibling, parent, node_idx):
        """Borrow a key from left sibling."""
        if node.is_leaf:
            # Borrow from left sibling leaf
            node.keys.insert(0, left_sibling.keys.pop())
            node.values.insert(0, left_sibling.values.pop())
            parent.keys[node_idx - 1] = node.keys[0]
        else:
            # Borrow from left sibling internal node
            node.keys.insert(0, parent.keys[node_idx - 1])
            parent.keys[node_idx - 1] = left_sibling.keys.pop()
            node.children.insert(0, left_sibling.children.pop())

    def _borrow_from_right(self, node, right_sibling, parent, node_idx):
        """Borrow a key from right sibling."""
        if node.is_leaf:
            # Borrow from right sibling leaf
            node.keys.append(right_sibling.keys.pop(0))
            node.values.append(right_sibling.values.pop(0))
            parent.keys[node_idx] = right_sibling.keys[0]
        else:
            # Borrow from right sibling internal node
            node.keys.append(parent.keys[node_idx])
            parent.keys[node_idx] = right_sibling.keys.pop(0)
            node.children.append(right_sibling.children.pop(0))

    def _merge_with_left(self, node, parent, node_idx):
        """Merge node with left sibling."""
        left_sibling = parent.children[node_idx - 1]

        if node.is_leaf:
            # Merge leaf nodes
            left_sibling.keys.extend(node.keys)
            left_sibling.values.extend(node.values)
            left_sibling.next = node.next
        else:
            # Merge internal nodes
            left_sibling.keys.append(parent.keys[node_idx - 1])
            left_sibling.keys.extend(node.keys)
            left_sibling.children.extend(node.children)

        # Remove key and child from parent
        parent.keys.pop(node_idx - 1)
        parent.children.pop(node_idx)

        # Handle parent underflow
        if parent != self.root and parent.is_underflow():
            self._handle_underflow(parent)
        elif parent == self.root and len(parent.keys) == 0:
            self.root = left_sibling

    def _merge_with_right(self, node, parent, node_idx):
        """Merge node with right sibling."""
        right_sibling = parent.children[node_idx + 1]

        if node.is_leaf:
            # Merge leaf nodes
            node.keys.extend(right_sibling.keys)
            node.values.extend(right_sibling.values)
            node.next = right_sibling.next
        else:
            # Merge internal nodes
            node.keys.append(parent.keys[node_idx])
            node.keys.extend(right_sibling.keys)
            node.children.extend(right_sibling.children)

        # Remove key and child from parent
        parent.keys.pop(node_idx)
        parent.children.pop(node_idx + 1)

        # Handle parent underflow
        if parent != self.root and parent.is_underflow():
            self._handle_underflow(parent)
        elif parent == self.root and len(parent.keys) == 0:
            self.root = node

    def range_query(self, start_key, end_key):
        """Return all key-value pairs in the range [start_key, end_key]."""
        result = []
        leaf = self._find_leaf(start_key)

        while leaf:
            for i, key in enumerate(leaf.keys):
                if start_key <= key <= end_key:
                    result.append((key, leaf.values[i]))
                elif key > end_key:
                    return result
            leaf = leaf.next

        return result

    def get_all(self):
        """Return all key-value pairs in sorted order."""
        result = []
        leaf = self.leftmost_leaf

        while leaf:
            for i, key in enumerate(leaf.keys):
                result.append((key, leaf.values[i]))
            leaf = leaf.next

        return result

    def get_height(self):
        """Return the height of the tree."""
        if self.root.is_leaf:
            return 1

        height = 1
        node = self.root
        while not node.is_leaf:
            height += 1
            node = node.children[0]

        return height

    def is_empty(self):
        """Check if the tree is empty."""
        return len(self.root.keys) == 0

    def __len__(self):
        """Return the number of keys in the tree."""
        count = 0
        leaf = self.leftmost_leaf

        while leaf:
            count += len(leaf.keys)
            leaf = leaf.next

        return count

    def __contains__(self, key):
        """Check if key exists in the tree."""
        return self.search(key) is not None

    def __repr__(self):
        """String representation of the tree."""
        if self.is_empty():
            return f"BPlusTree(order={self.order}, empty)"
        return f"BPlusTree(order={self.order}, size={len(self)}, height={self.get_height()})"

    def print_tree(self):
        """Print tree structure for visualization."""
        if self.is_empty():
            print("Empty tree")
            return

        queue = [(self.root, 0)]
        current_level = 0

        while queue:
            node, level = queue.pop(0)

            if level > current_level:
                print()
                current_level = level

            print(f"[{', '.join(map(str, node.keys))}]", end=" ")

            if not node.is_leaf:
                for child in node.children:
                    queue.append((child, level + 1))

        print()
