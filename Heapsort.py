import time


def swap(arr, maximum, largest):
    if maximum != largest:
        array = arr[largest]
        arr[largest] = arr[maximum]
        arr[maximum] = array


def leftchild(largest_index):
    left = largest_index * 2 + 1
    return left


def rightchild(largest_index):
    right = largest_index * 2 + 2
    return right


def heap_sort(array):
    start_time = time.time()
    n = len(array)
    for i in range(((n - 1) // 2), -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        swap(array, 0, i)
        n -= 1
        heapify(array, n, 0)
    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed


def heapify(arr, heap, largest_index):
    max_index = largest_index
    left_child = leftchild(max_index)
    right_child = rightchild(max_index)
    if left_child < heap and arr[left_child] > arr[max_index]:
        max_index = left_child
    if right_child < heap and arr[right_child] > arr[max_index]:
        max_index = right_child
    if max_index != largest_index:
        swap(arr, max_index, largest_index)
        heapify(arr, heap, max_index)