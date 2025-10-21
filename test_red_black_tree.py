"""
Test file for Red-Black Tree implementation
"""

from red_black_tree import RedBlackTree


def test_basic_operations():
    print("=== Test Basic Operations ===")
    rbt = RedBlackTree()

    # Test insertion
    print("Inserting keys: 10, 20, 30, 15, 25, 5")
    rbt.insert(10, "value10")
    rbt.insert(20, "value20")
    rbt.insert(30, "value30")
    rbt.insert(15, "value15")
    rbt.insert(25, "value25")
    rbt.insert(5, "value5")

    print(f"Tree: {rbt}")
    print(f"Inorder traversal: {rbt.inorder_traversal()}")

    # Test search
    print("\n--- Search Operations ---")
    print(f"Search key 15: {rbt.search(15)}")
    print(f"Search key 100: {rbt.search(100)}")
    print(f"Contains 20: {20 in rbt}")
    print(f"Contains 100: {100 in rbt}")

    # Test deletion
    print("\n--- Deletion Operations ---")
    print(f"Deleting key 20: {rbt.delete(20)}")
    print(f"Inorder traversal after deletion: {rbt.inorder_traversal()}")
    print(f"Search key 20 after deletion: {rbt.search(20)}")

    print()


def test_large_dataset():
    print("=== Test Large Dataset ===")
    rbt = RedBlackTree()

    # Insert 100 elements
    print("Inserting 100 elements...")
    for i in range(100):
        rbt.insert(i, f"value{i}")

    print(f"Tree size: {len(rbt)}")
    print(f"Tree height: {rbt.get_height()}")

    # Search for some elements
    print("\n--- Random Search Tests ---")
    test_keys = [0, 25, 50, 75, 99, 100]
    for key in test_keys:
        result = rbt.search(key)
        print(f"Search key {key}: {result}")

    # Delete some elements
    print("\n--- Deletion Tests ---")
    delete_keys = [0, 25, 50, 75, 99]
    for key in delete_keys:
        rbt.delete(key)

    print(f"Tree size after deletions: {len(rbt)}")
    print(f"Tree height after deletions: {rbt.get_height()}")

    print()


def test_update_values():
    print("=== Test Update Values ===")
    rbt = RedBlackTree()

    # Insert
    rbt.insert(10, "initial_value")
    print(f"Initial value for key 10: {rbt.search(10)}")

    # Update
    rbt.insert(10, "updated_value")
    print(f"Updated value for key 10: {rbt.search(10)}")

    print()


def test_traversals():
    print("=== Test Traversals ===")
    rbt = RedBlackTree()

    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        rbt.insert(key, f"value{key}")

    print(f"Inorder traversal: {rbt.inorder_traversal()}")
    print(f"Preorder traversal: {rbt.preorder_traversal()}")

    print()


def test_edge_cases():
    print("=== Test Edge Cases ===")

    # Empty tree
    rbt = RedBlackTree()
    print(f"Empty tree: {rbt.is_empty()}")
    print(f"Empty tree size: {len(rbt)}")
    print(f"Search in empty tree: {rbt.search(10)}")
    print(f"Delete from empty tree: {rbt.delete(10)}")

    # Single element
    rbt.insert(1, "value1")
    print(f"\nAfter inserting one element:")
    print(f"Is empty: {rbt.is_empty()}")
    print(f"Size: {len(rbt)}")
    print(f"Height: {rbt.get_height()}")

    # Delete single element
    rbt.delete(1)
    print(f"\nAfter deleting the only element:")
    print(f"Is empty: {rbt.is_empty()}")
    print(f"Size: {len(rbt)}")

    print()


def test_duplicate_keys():
    print("=== Test Duplicate Keys ===")
    rbt = RedBlackTree()

    # Insert duplicate keys
    rbt.insert(10, "first")
    rbt.insert(20, "second")
    rbt.insert(10, "third")  # This should update the value

    print(f"Value for key 10: {rbt.search(10)}")
    print(f"Tree size: {len(rbt)}")
    print(f"Inorder traversal: {rbt.inorder_traversal()}")

    print()


def main():
    print("=" * 50)
    print("Red-Black Tree Test Suite")
    print("=" * 50)
    print()

    test_basic_operations()
    test_large_dataset()
    test_update_values()
    test_traversals()
    test_edge_cases()
    test_duplicate_keys()

    print("=" * 50)
    print("All tests completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
