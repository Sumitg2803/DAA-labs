# Recursive Binary Search
def binary_search_recursive(arr, low, high, key):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search_recursive(arr, low, mid - 1, key)
        else:
            return binary_search_recursive(arr, mid + 1, high, key)
    return -1


# Non-Recursive Binary Search
def binary_search_iterative(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1

    return -1


# Main Program
arr = list(map(int, input("Enter sorted elements: ").split()))
key = int(input("Enter key to search: "))

# Recursive search
result_rec = binary_search_recursive(arr, 0, len(arr)-1, key)

# Iterative search
result_itr = binary_search_iterative(arr, key)

# Output
if result_rec != -1:
    print("Recursive: Element found at index", result_rec)
else:
    print("Recursive: Element not found")

if result_itr != -1:
    print("Non-Recursive: Element found at index", result_itr)
else:
    print("Non-Recursive: Element not found")