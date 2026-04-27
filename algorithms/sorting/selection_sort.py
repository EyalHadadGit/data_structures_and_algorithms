def selection_sort(custom_list):
    n=len(custom_list)
    for i in range(n-1):
        min_idx=i
        for j in range(i+1,n):
            if custom_list[j]<custom_list[min_idx]:
                min_idx=j
        custom_list[i],custom_list[min_idx]=custom_list[min_idx],custom_list[i]
    return custom_list