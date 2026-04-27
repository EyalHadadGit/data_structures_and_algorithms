import numpy as np
from math import ceil
from Final.algorithms.sorting.insert_sort import insert_sort

def bucket_sort(custom_list):
    if len(custom_list) == 0:
        return []
    sorted_lst = []
    number_of_buckets = round(np.sqrt(len(custom_list)))
    maximum_value = max(custom_list)
    bucket_list = [[] for _ in range(number_of_buckets)]
    for element in custom_list:
        index = ceil(element * number_of_buckets / maximum_value) - 1
        if index == number_of_buckets:
            index -= 1
        bucket_list[index].append(element)
    for i in range(number_of_buckets):
        sorted_lst += insert_sort(bucket_list[i])
    return sorted_lst