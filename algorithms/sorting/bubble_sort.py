def bubble_sort(custom_list):
    for j in range(len(custom_list) - 1, 0, -1):
        swapped = False
        for i in range(j):
            if custom_list[i] > custom_list[i + 1]:
                custom_list[i], custom_list[i + 1] = custom_list[i + 1], custom_list[i]
                swapped = True
        if not swapped:
            break
    return custom_list