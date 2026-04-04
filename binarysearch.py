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

m=list(map(int,input("please enter numbers: ").split()))
key=int(input("please enter a key: "))

for i in m:
    if i==key:
        print("i found the key")
        break
else:
    print("the key was not found")
