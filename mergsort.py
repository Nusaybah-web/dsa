def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergerun(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=mergerun(arr[:mid])
    right=mergerun(arr[mid:])
    return merge(left,right)

print(mergerun([23,45,76,27,28,91,75,36]))