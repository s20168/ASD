import time


def bubble_sort(our_list):
    start_time = time.time()
    has_swapped = True

    num_of_iterations = 0

    while has_swapped:
        has_swapped = False
        for i in range(len(our_list) - num_of_iterations - 1):
            if our_list[i] > our_list[i + 1]:

                our_list[i], our_list[i + 1] = our_list[i + 1], our_list[i]
                has_swapped = True
        num_of_iterations += 1
    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed