def quick(lst):
   quickSort(lst,0,len(lst)-1)

def quickSort(lst,start,end):
   if start<end:

       pivot = partition(lst,start,end)

       quickSort(lst,start,pivot-1)
       quickSort(lst,pivot+1,end)


def partition(lst,start,end):
   pivotvalue = lst[start]

   left = start+1
   right = end

   done = False
   while not done:

       while left <= right and lst[left] <= pivotvalue:
           left = left + 1

       while lst[right] >= pivotvalue and right >= left:
           right = right -1

       if right < left:
           done = True
       else:
           temp = lst[left]
           lst[left] = lst[right]
           lst[right] = temp

   temp = lst[start]
   lst[start] = lst[right]
   lst[right] = temp
   return right

lst = [54,26,93,17,77,31,44,55,20]
quick(lst)
print(lst)
