"""class stack:
    def __init__(self,n):
        self.stack=[]
        self.n=n
    def push(self,a):
        if len(self.stack)<self.n:
            self.stack.append(a)
        else:
            print("the stack is full")
    def pop(self):
        if len(self.stack)==0:
            print("the sack is empty")
        else:
            self.stack.pop(-1)
    def top(self):
        if len(self.stack)==0:
            print("the sack is empty")
        else:
            return self.stack[-1]
    def size(self):
        return len(self.stack)
    def display(self):
        print(self.stack)"""

#program to reverse a string with stack

"""def wordreverse(inp):
    stack=[]
    for i in inp:
        stack.append(i)
    reversed=""
    while len(stack)>0:
        reversed+=stack.pop()
    return reversed

w=wordreverse("python")

print(w)"""

#program to simulate undo

"""stack=[]
current=""

def add(word):
    global current
    stack.append(current)
    current+=word+ " "
def undo():
    global current
    if len(stack)>0:
        current=stack.pop()
    else:
        print("nothing to undo")

add("hello")

print(current)

add("world")

print(current)

undo()

print(current)"""

def merge(arr):
    l=[]
    for i in arr:
        if i%2==0:
            l.append(i)
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        merge(left)
        merge(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                l[k]=left[i]
                i+=1
            else:
                l[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            l[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            l[k]=right[j]
            j+=1
            k+=1
    return l
    
array=[23,45,76,27,28,91,75,36]
print(merge(array))