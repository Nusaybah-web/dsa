"""def names(l,t):# list and target word
    l.sort()
    low,high=0,len(l)-1
    steps=0
    while low<=high:
        steps+=1
        mid=(low+high)//2
        guess=l[mid]
        print(f"step {steps}: searching in the range {l[low:high+1]}, guessed: {guess}")
        if guess==t:
            print(f"target {t} was found at index {mid}")
            return mid
        elif guess>t:
            high=mid-1
        else:
            low=mid+1
    print("target not found")
    return -1


lis=["apple","banana","pear","grapes","orange","lychee","dragonfrute","pineapple"]

target="banana"

call=names(lis,target)

num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

tar=7

c=names(num,tar)
"""
#linear search

"""m=list(map(int,input("please enter numbers: ").split()))
key=int(input("please enter a key: "))

for i in m:
    if i==key:
        print("i found the key")
        break
else:
    print("the key was not found")
"""

"""def root(x):
    low=0
    high=x
    ans=0
    while low<high:
        mid=(low+high)//2
        if mid*mid==x:
            return mid
        elif mid*mid<x:
            ans=mid#possible answer
            low=mid+1
        else:
            high=mid-1
    return ans

call=(root(18))
print(call)"""

"""def midd(l):
    arr=l
    low=0
    high=len(l)-1
    while low!=high:
        mid=(low+high)//2
        if arr[mid]==mid:
            low=mid+1
        else:
            high=mid-1
    return low


l=[0,1,2,3,4,6,7,8,9]
print(midd(l))"""

"""def compare(l,t):
    low=0
    high=len(l)-1
    while low!=high:
        mid=(low+high)//2
        guess=l[mid]
        if guess==t:
            return mid
        elif guess>t:
            high=mid-1
        elif guess<mid:
            low=mid+1
    return mid


numbers=list(range(1, 1000001))
print(compare(numbers,1000001))"""

import time

num=list(range(1,500))
target=350

#lenier search
def lenier(a,t):
    for i in range(len(a)):
        if a[i]==t:
            return i
    return -1

def binary(a,t):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(low+high)//2
        guess=a[mid]
        if guess==t:
            return mid
        elif guess>t:
            high=mid-1
        elif guess<mid:
            low=mid+1
    return -1

#mesuring lenier search
st=time.time()
li=lenier(num,target)
et=time.time()
print(f"lenier search took {et-st} seconds")

#binary
bst=time.time()
bi=binary(num,target)
bet=time.time()
print(f"binary search took {bet-bst} seconds")