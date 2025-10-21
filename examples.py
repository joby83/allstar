"""
Usage examples for Red-Black Tree and B+ Tree
"""

from red_black_tree import RedBlackTree
from bplus_tree import BPlusTree


def red_black_tree_example():
    print("=" * 60)
    print("Red-Black Tree Example")
    print("=" * 60)

    # Create a Red-Black Tree
    rbt = RedBlackTree()

    # Insert some data
    print("\n1. Inserting student records...")
    students = [
        (101, "Alice"),
        (105, "Bob"),
        (103, "Charlie"),
        (107, "David"),
        (102, "Eve"),
        (106, "Frank"),
        (104, "Grace")
    ]

    for student_id, name in students:
        rbt.insert(student_id, name)
        print(f"   Inserted: ID={student_id}, Name={name}")

    print(f"\n   Tree info: {rbt}")

    # Search for students
    print("\n2. Searching for students...")
    search_ids = [103, 106, 999]
    for student_id in search_ids:
        result = rbt.search(student_id)
        if result:
            print(f"   Student ID {student_id}: {result}")
        else:
            print(f"   Student ID {student_id}: Not found")

    # Display all students in sorted order
    print("\n3. All students (sorted by ID):")
    for student_id, name in rbt.inorder_traversal():
        print(f"   ID={student_id}, Name={name}")

    # Delete a student
    print("\n4. Deleting student with ID 105...")
    rbt.delete(105)
    print("   After deletion:")
    for student_id, name in rbt.inorder_traversal():
        print(f"   ID={student_id}, Name={name}")

    print()


def bplus_tree_example():
    print("=" * 60)
    print("B+ Tree Example")
    print("=" * 60)

    # Create a B+ Tree with order 4
    bpt = BPlusTree(order=4)

    # Insert some data (product inventory)
    print("\n1. Inserting product inventory...")
    products = [
        (150, "Laptop"),
        (200, "Mouse"),
        (100, "Keyboard"),
        (175, "Monitor"),
        (125, "Headphones"),
        (225, "Webcam"),
        (110, "USB Cable"),
        (190, "HDMI Cable"),
        (160, "Microphone"),
        (210, "Speaker")
    ]

    for product_id, name in products:
        bpt.insert(product_id, name)
        print(f"   Inserted: ID={product_id}, Name={name}")

    print(f"\n   Tree info: {bpt}")

    # Search for products
    print("\n2. Searching for products...")
    search_ids = [125, 200, 999]
    for product_id in search_ids:
        result = bpt.search(product_id)
        if result:
            print(f"   Product ID {product_id}: {result}")
        else:
            print(f"   Product ID {product_id}: Not found")

    # Range query - find all products in a price range
    print("\n3. Range query - Products with IDs between 150-200:")
    for product_id, name in bpt.range_query(150, 200):
        print(f"   ID={product_id}, Name={name}")

    # Display all products in sorted order
    print("\n4. All products (sorted by ID):")
    for product_id, name in bpt.get_all():
        print(f"   ID={product_id}, Name={name}")

    # Delete a product
    print("\n5. Deleting product with ID 200...")
    bpt.delete(200)
    print("   Remaining products:")
    for product_id, name in bpt.get_all():
        print(f"   ID={product_id}, Name={name}")

    # Another range query
    print("\n6. Range query - Products with IDs between 100-130:")
    for product_id, name in bpt.range_query(100, 130):
        print(f"   ID={product_id}, Name={name}")

    print()


def performance_comparison():
    print("=" * 60)
    print("Performance Comparison")
    print("=" * 60)

    import time

    n = 10000  # Number of elements

    # Red-Black Tree
    print(f"\n1. Red-Black Tree - Inserting {n} elements...")
    rbt = RedBlackTree()
    start_time = time.time()
    for i in range(n):
        rbt.insert(i, f"value{i}")
    rbt_insert_time = time.time() - start_time
    print(f"   Insert time: {rbt_insert_time:.4f} seconds")
    print(f"   Tree height: {rbt.get_height()}")

    print(f"\n2. Red-Black Tree - Searching {n} elements...")
    start_time = time.time()
    for i in range(n):
        rbt.search(i)
    rbt_search_time = time.time() - start_time
    print(f"   Search time: {rbt_search_time:.4f} seconds")

    # B+ Tree
    print(f"\n3. B+ Tree (order=5) - Inserting {n} elements...")
    bpt = BPlusTree(order=5)
    start_time = time.time()
    for i in range(n):
        bpt.insert(i, f"value{i}")
    bpt_insert_time = time.time() - start_time
    print(f"   Insert time: {bpt_insert_time:.4f} seconds")
    print(f"   Tree height: {bpt.get_height()}")

    print(f"\n4. B+ Tree - Searching {n} elements...")
    start_time = time.time()
    for i in range(n):
        bpt.search(i)
    bpt_search_time = time.time() - start_time
    print(f"   Search time: {bpt_search_time:.4f} seconds")

    print(f"\n5. B+ Tree - Range query [1000, 2000]...")
    start_time = time.time()
    result = bpt.range_query(1000, 2000)
    bpt_range_time = time.time() - start_time
    print(f"   Range query time: {bpt_range_time:.4f} seconds")
    print(f"   Results found: {len(result)}")

    print("\n" + "=" * 60)
    print("Summary:")
    print(f"  Red-Black Tree: Insert={rbt_insert_time:.4f}s, Search={rbt_search_time:.4f}s")
    print(f"  B+ Tree: Insert={bpt_insert_time:.4f}s, Search={bpt_search_time:.4f}s")
    print(f"  B+ Tree has efficient range queries: {bpt_range_time:.4f}s")
    print("=" * 60)


def main():
    red_black_tree_example()
    print("\n\n")
    bplus_tree_example()
    print("\n\n")
    performance_comparison()


if __name__ == "__main__":
    main()
