def heapify(custom_list,n,i):
    largest=i
    left_child_index,right_child_index=2*i+1,2*i+2
    if left_child_index<n and custom_list[left_child_index]>custom_list[largest]:
        largest=left_child_index
    if right_child_index<n and custom_list[right_child_index]>custom_list[largest]:
        largest=right_child_index
    if largest!=i:
        custom_list[i],custom_list[largest]=custom_list[largest],custom_list[i]
        heapify(custom_list,n,largest)

def heap_sort(custom_list):
    n=len(custom_list)
    for i in range(n//2-1,-1,-1):
        heapify(custom_list,n,i)
    for i in range(n-1,0,-1):
        custom_list[i],custom_list[0]=custom_list[0],custom_list[i]
        heapify(custom_list,i,0)
    return custom_list