def merge_sort(custom_list): # breaks down a list to sub lists of length 2
    if len(custom_list) <= 1:
        return custom_list
    mid = len(custom_list) // 2
    left = merge_sort(custom_list[:mid])
    right = merge_sort(custom_list[mid:])
    return merge(left, right) # o(nlogn)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result