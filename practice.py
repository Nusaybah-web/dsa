def merge(arr):
    print("splitting ",arr)
    l=[]
    for i in arr:
        if i%2==0:
            l.append(i)
    if len(arr)<=1:
        return arr
    mid=len(l)//2
    left=l[:mid]
    right=l[mid:]
    i=j=0
    k=[]
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            k.append(right[j])
            j+=1
        else:
            k.append(left[i])
            i+=1
    k.extend(left[i:])
    k.extend(right[j:])
    print("merging ",k)
    return k
    
array=[23,45,76,27,28,91,75,36]
print(merge(array))

#palindrum searcher

"""def wordreverse(inp):
    stack=[]
    for i in inp:
        stack.append(i)
    for i in inp:
        if i!=stack.pop():
            return False
    return True
        

w=wordreverse("racecar")

print(w)"""

#binary converter

"""def binary(num):
    stack=[]
    while num>0:
        r=num%2
        stack.append(r)
        num=num//2
    binary=""
    while stack:
        binary+=str(stack.pop())
    return binary

b=binary(10)

print(b)"""

