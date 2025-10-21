"""
Test file for B+ Tree implementation
"""

from bplus_tree import BPlusTree


def test_basic_operations():
    print("=== Test Basic Operations ===")
    bpt = BPlusTree(order=4)

    # Test insertion
    print("Inserting keys: 10, 20, 30, 15, 25, 5")
    bpt.insert(10, "value10")
    bpt.insert(20, "value20")
    bpt.insert(30, "value30")
    bpt.insert(15, "value15")
    bpt.insert(25, "value25")
    bpt.insert(5, "value5")

    print(f"Tree: {bpt}")
    print(f"All keys (sorted): {bpt.get_all()}")

    # Test search
    print("\n--- Search Operations ---")
    print(f"Search key 15: {bpt.search(15)}")
    print(f"Search key 100: {bpt.search(100)}")
    print(f"Contains 20: {20 in bpt}")
    print(f"Contains 100: {100 in bpt}")

    # Test range query
    print("\n--- Range Query ---")
    print(f"Range query [10, 25]: {bpt.range_query(10, 25)}")

    # Test deletion
    print("\n--- Deletion Operations ---")
    print(f"Deleting key 20: {bpt.delete(20)}")
    print(f"All keys after deletion: {bpt.get_all()}")
    print(f"Search key 20 after deletion: {bpt.search(20)}")

    print()


def test_large_dataset():
    print("=== Test Large Dataset ===")
    bpt = BPlusTree(order=5)

    # Insert 100 elements
    print("Inserting 100 elements...")
    for i in range(100):
        bpt.insert(i, f"value{i}")

    print(f"Tree size: {len(bpt)}")
    print(f"Tree height: {bpt.get_height()}")

    # Search for some elements
    print("\n--- Random Search Tests ---")
    test_keys = [0, 25, 50, 75, 99, 100]
    for key in test_keys:
        result = bpt.search(key)
        print(f"Search key {key}: {result}")

    # Range query
    print("\n--- Range Query Tests ---")
    print(f"Range [20, 30]: {bpt.range_query(20, 30)}")
    print(f"Range [90, 99]: {bpt.range_query(90, 99)}")

    # Delete some elements
    print("\n--- Deletion Tests ---")
    delete_keys = [0, 25, 50, 75, 99]
    for key in delete_keys:
        bpt.delete(key)

    print(f"Tree size after deletions: {len(bpt)}")
    print(f"Tree height after deletions: {bpt.get_height()}")

    print()


def test_different_orders():
    print("=== Test Different Orders ===")

    for order in [3, 4, 5, 6]:
        print(f"\n--- Order {order} ---")
        bpt = BPlusTree(order=order)

        # Insert 20 elements
        for i in range(20):
            bpt.insert(i, f"value{i}")

        print(f"Tree size: {len(bpt)}")
        print(f"Tree height: {bpt.get_height()}")

    print()


def test_range_queries():
    print("=== Test Range Queries ===")
    bpt = BPlusTree(order=4)

    # Insert elements
    keys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for key in keys:
        bpt.insert(key, f"value{key}")

    print(f"All keys: {bpt.get_all()}")

    # Various range queries
    print("\n--- Range Query Results ---")
    ranges = [(10, 30), (40, 70), (80, 100), (15, 45), (0, 100), (200, 300)]
    for start, end in ranges:
        result = bpt.range_query(start, end)
        print(f"Range [{start}, {end}]: {result}")

    print()


def test_update_values():
    print("=== Test Update Values ===")
    bpt = BPlusTree(order=4)

    # Insert
    bpt.insert(10, "initial_value")
    print(f"Initial value for key 10: {bpt.search(10)}")

    # Update
    bpt.insert(10, "updated_value")
    print(f"Updated value for key 10: {bpt.search(10)}")
    print(f"Tree size (should be 1): {len(bpt)}")

    print()


def test_edge_cases():
    print("=== Test Edge Cases ===")

    # Empty tree
    bpt = BPlusTree(order=4)
    print(f"Empty tree: {bpt.is_empty()}")
    print(f"Empty tree size: {len(bpt)}")
    print(f"Search in empty tree: {bpt.search(10)}")
    print(f"Delete from empty tree: {bpt.delete(10)}")
    print(f"Range query in empty tree: {bpt.range_query(1, 10)}")

    # Single element
    bpt.insert(1, "value1")
    print(f"\nAfter inserting one element:")
    print(f"Is empty: {bpt.is_empty()}")
    print(f"Size: {len(bpt)}")
    print(f"Height: {bpt.get_height()}")
    print(f"All keys: {bpt.get_all()}")

    # Delete single element
    bpt.delete(1)
    print(f"\nAfter deleting the only element:")
    print(f"Is empty: {bpt.is_empty()}")
    print(f"Size: {len(bpt)}")

    print()


def test_sequential_insertion():
    print("=== Test Sequential Insertion ===")
    bpt = BPlusTree(order=4)

    # Insert in ascending order
    print("Inserting 1-20 in order...")
    for i in range(1, 21):
        bpt.insert(i, f"value{i}")

    print(f"Tree: {bpt}")
    print(f"First 5 elements: {bpt.get_all()[:5]}")
    print(f"Last 5 elements: {bpt.get_all()[-5:]}")

    print()


def test_reverse_insertion():
    print("=== Test Reverse Insertion ===")
    bpt = BPlusTree(order=4)

    # Insert in descending order
    print("Inserting 20-1 in reverse order...")
    for i in range(20, 0, -1):
        bpt.insert(i, f"value{i}")

    print(f"Tree: {bpt}")
    print(f"All elements should still be sorted:")
    print(f"First 5 elements: {bpt.get_all()[:5]}")
    print(f"Last 5 elements: {bpt.get_all()[-5:]}")

    print()


def test_tree_structure():
    print("=== Test Tree Structure ===")
    bpt = BPlusTree(order=4)

    # Insert elements
    print("Inserting keys: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
    for i in range(1, 11):
        bpt.insert(i, f"value{i}")

    print(f"\nTree: {bpt}")
    print("Tree structure:")
    bpt.print_tree()

    print()


def test_stress_deletion():
    print("=== Test Stress Deletion ===")
    bpt = BPlusTree(order=5)

    # Insert many elements
    print("Inserting 50 elements...")
    for i in range(50):
        bpt.insert(i, f"value{i}")

    print(f"Initial size: {len(bpt)}")

    # Delete all elements
    print("Deleting all elements...")
    for i in range(50):
        bpt.delete(i)

    print(f"Size after all deletions: {len(bpt)}")
    print(f"Is empty: {bpt.is_empty()}")

    print()


def main():
    print("=" * 50)
    print("B+ Tree Test Suite")
    print("=" * 50)
    print()

    test_basic_operations()
    test_large_dataset()
    test_different_orders()
    test_range_queries()
    test_update_values()
    test_edge_cases()
    test_sequential_insertion()
    test_reverse_insertion()
    test_tree_structure()
    test_stress_deletion()

    print("=" * 50)
    print("All tests completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
