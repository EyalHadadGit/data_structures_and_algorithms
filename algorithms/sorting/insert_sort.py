def insert_sort(custom_list):
    if custom_list is None:
        raise ValueError("Input cannot be None")
    if len(custom_list)<=1:
        return custom_list
    for i in range(1,len(custom_list)):
        key=custom_list[i]
        j=i-1
        while j>=0 and custom_list[j]>key:
            custom_list[j+1]=custom_list[j]
            j-=1
        custom_list[j+1]=key
    return custom_list
