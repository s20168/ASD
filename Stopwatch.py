import random, sys

from Heapsort import heap_sort
from Quicksort import quick_sort_test
from Bubblesort import bubble_sort
sys.setrecursionlimit(55000)


class Stopwatch:
    def count(self):
        random_array_high = []
        for i in range(0, 20000):
            n = random.randint(0, 1)
            random_array_high.append(n)

        sorted_array = sorted(random_array_high)
        reverse_sorted_array = list(reversed(sorted_array))
        random_heapsort_time = 0
        random_quicksort_time = 0
        random_bubblesort_time = 0


        sorted_heapsort_time = 0
        sorted_quicksort_time = 0
        sorted_bubblesort_time = 0

        reverse_sorted_bubblesort_time = 0
        reverse_sorted_heapsort_time = 0
        reverse_sorted_quicksort_time = 0

        random_heapsort_time += heap_sort(random_array_high)
        random_quicksort_time += quick_sort_test(random_array_high)
        random_bubblesort_time += bubble_sort(random_array_high)

        sorted_heapsort_time += heap_sort(sorted_array)
        sorted_quicksort_time += quick_sort_test(sorted_array)
        sorted_bubblesort_time += bubble_sort(sorted_array)

        reverse_sorted_heapsort_time += heap_sort(reverse_sorted_array)
        reverse_sorted_quicksort_time += quick_sort_test(reverse_sorted_array)
        reverse_sorted_bubblesort_time += bubble_sort(reverse_sorted_array)

        print(str("RandomHeapsort: ") + str("{0:.15f}".format(random_heapsort_time / 100)))
        print(str("RandomQuicksort: ") + str("{0:.15f}".format(random_quicksort_time / 100)))
        print(str("RandomBubblesort: ") + str("{0:.15f}".format(random_bubblesort_time / 100)))

        print(str("SortedHeapsort: ") + str("{0:.15f}".format(sorted_heapsort_time / 100)))
        print(str("SortedQuicksort: ") + str("{0:.15f}".format(sorted_quicksort_time / 100)))
        print(str("SortedBubblesort: ") + str("{0:.15f}".format(sorted_bubblesort_time / 100)))

        print(str("ReverseSortedHeapsort: ") + str("{0:.15f}".format(reverse_sorted_heapsort_time / 100)))
        print(str("ReverseSortedQuicksort: ") + str("{0:.15f}".format(reverse_sorted_quicksort_time / 100)))
        print(str("ReverseSortedBubblesort: ") + str("{0:.15f}".format(reverse_sorted_bubblesort_time / 100)))


if __name__ == '__main__':
    xx = Stopwatch()
    xx.count()