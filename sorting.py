list=[3,4,6,2,1,3,57,9,5,42,3,6,89]
#list.sort(reverse=True)

"""for i in range(len(list)):
    for j in range(i,len(list)):
        if list[i]<list[j]:
            list[i],list[j]=list[j],list[i]


print(list)"""

#insertion sort
"""for i in range(1,len(list)):
    key=list[i]
    j=i-1
    while j>=0 and list[j]>key:
        list[j+1]=list[j]
        j-=1
    list[j+1]=key

print(list)
"""
#word length sorter

"""fruit=["apple", "kiwi", "banana", "pie", "date"]

for i in range(1,len(fruit)):
    key=fruit[i]
    j=i-1
    while j>=0 and len(fruit[j])>len(key):
        fruit[j+1]=fruit[j]
        j-=1
    fruit[j+1]=key

print(fruit)
"""
#second digit sorter

num=[15, 32, 59, 21, 48]

for i in range(1,len(num)):
    key=num[i]
    j=i-1
    while j>=0 and num[j]%10>key%10:
        num[j+1]=num[j]
        j-=1
    num[j+1]=key

print(num)

for i in range(len(num)):
    for j in range(0,len(num)-i-1):
        if num[j]%10>num[j+1]%10:
            num[j],num[j+1]=num[j+1],num[j]

print(num)