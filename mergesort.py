def mergeSort(lst):
    print("Splitting ",lst)
    if len(lst)>1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]

        mergeSort(l)
        mergeSort(r)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < rightf[j]:
                lst[k]=left[i]
                i=i+1
            else:
                lst[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            lst[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
        	lst[k]=right[j]
        	j=j+1
        	k=k+1
    print("Merging ",lst)

lst = [1]
mergeSort(lst)
