# Function to perform Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        # Partition index
        pi = partition(arr, low, high)

        # Recursively sort left and right parts
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Function to partition the array
def partition(arr, low, high):
    pivot = arr[high]   # Last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot at correct position
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


# Main program
arr = list(map(int, input("Enter elements: ").split()))

quick_sort(arr, 0, len(arr)-1)

print("Sorted array:", arr)