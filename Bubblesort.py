import time


def bubble_sort(arr):
    start_time = time.time()
    has_swapped = True

    num_of_iterations = 0

    while has_swapped:
        has_swapped = False
        for i in range(len(arr) - num_of_iterations - 1):
            if arr[i] > arr[i + 1]:

                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                has_swapped = True
        num_of_iterations += 1
    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed