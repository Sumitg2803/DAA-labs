# Function to heapify a subtree rooted at index i
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)   # Recursive call

# Recursive Heap Sort function
def heap_sort(arr, n):
    if n <= 1:
        return

    # Build heap (max heap)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # Move root to end
    arr[0], arr[n-1] = arr[n-1], arr[0]

    # Recursive call for remaining array
    heap_sort(arr, n-1)


# Main program
arr = list(map(int, input("Enter elements: ").split()))
n = len(arr)

heap_sort(arr, n)

print("Sorted array:", arr)