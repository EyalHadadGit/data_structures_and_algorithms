def quick_sort(custom_list):
    if len(custom_list)<=1:
        return custom_list
    pivot=custom_list[0]
    left=[]
    right=[]
    for i in range(1,len(custom_list)):
        if custom_list[i]<pivot:
            left.append(custom_list[i])
        else:
            right.append(custom_list[i])
    return quick_sort(left)+[pivot] + quick_sort(right)