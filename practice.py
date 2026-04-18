"""def m(l,r):
    result=[]
    i=j=0
    while i<len(l) and j<len(r):
        if l[i]>r[j]:
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
    result.extend(l[i:])
    result.extend(r[j:])
    return result

def merge(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge(arr[mid:])
    right=merge(arr[:mid])
    return m(right,left)

print(merge([23,45,76,27,28,91,75,36]))"""

#decending merge sort

"""def merge(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge(left)
        merge(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
        
    
array=[23,45,76,27,28,91,75,36]

merge(array)

print(array)
"""

#word length sorter

"""def sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        sort(left)
        sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if len(left[i])<len(right[j]):
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1

array=["elephant", "cat", "dog", "hippopotamus", "ant"]

sort(array)

print(array)"""

#merge two sorted lists

def sort(a,b):
    i=j=0
    l=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            l.append(a[i])
            i+=1
        else:
            l.append(b[j])
            j+=1
    while i<len(a):
        l.append(a[i])
        i+=1
    while j<len(b):
        l.append(b[j])
        j+=1

    return l
        
l1=[1,3,5,7,9]
l2=[0,2,4,6,8]

results=sort(l1,l2)

print(results)