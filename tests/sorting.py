from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.sorting.bucket_sort import bucket_sort
from algorithms.sorting.heap_sort import heap_sort
from algorithms.sorting.insert_sort import insert_sort
from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.quick_sort import quick_sort
from algorithms.sorting.selection_sort import selection_sort

test_cases = [
    [],                      # empty list
    [1],                     # single element
    [2, 1],                  # two elements reversed
    [1, 2],                  # two elements already sorted
    [5, 5, 5, 5],            # all duplicates
    [3, 1, 2, 1, 3],         # duplicates mixed
    [1, 2, 3, 4, 5],         # already sorted
    [5, 4, 3, 2, 1],         # reverse sorted
    [1, 3, 2, 5, 4],         # random small case
    [10, -1, 3, 0, -5],      # includes negative numbers
    [0, 0, 0, 0, 0],         # all zeros
    [1000000, 1, 999999],    # large values
]

for test in test_cases:
    sorted_test = sorted(test)
    assert bubble_sort(test) == sorted_test
    assert heap_sort(test) == sorted_test
    assert insert_sort(test) == sorted_test
    assert merge_sort(test) == sorted_test
    assert quick_sort(test) == sorted_test
    assert selection_sort(test) == sorted_test
    if len(sorted_test) == 0 or sorted_test[0] > 0: # bucket sort works only for positive numbers
        assert bucket_sort(test) == sorted_test

print('All tests passed!')
