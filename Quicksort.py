import time


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def partition(A, p, r):
    pivot = A[r]

    smaller = p

    for i in range(p, r):
        if A[i] <= pivot:
            A[smaller], A[i] = A[i], A[smaller]
            smaller = smaller + 1

    A[smaller], A[r] = A[r], A[smaller]

    return smaller


def quick_sort_test(A):
    start_time = time.time()
    quick_sort(A, 0, len(A) - 1)
    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed