# Array Implementation in Python

# Create an array
arr = [10, 20, 30, 40, 50]

# 1. Traverse
def traverse(arr):
    print("Array elements:")
    for item in arr:
        print(item, end=" ")
    print()

# 2. Search (Linear Search)
def search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# 3. Insert at index
def insert(arr, index, value):
    arr.insert(index, value)

# 4. Delete by value
def delete_by_value(arr, value):
    if value in arr:
        arr.remove(value)

# Example usage
if __name__ == "__main__":
    traverse(arr)
    print("Search 30:", search(arr, 30))  # Output: 2
    insert(arr, 2, 25)
    traverse(arr)  # Now includes 25
    delete_by_value(arr, 10)
    traverse(arr)  # 10 is removed