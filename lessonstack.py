class stack:
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
        print(self.stack)

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

stack=[]
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

print(current)