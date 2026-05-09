class queue:
    def __init__(self,size):
        self.queue=[None]*size
        self.front=0
        self.rear=0
        self.avabale=size
        self.size=size
    def enqueue(self,item):
        if self.avabale==0:
            print("queue overflow")
        else:
            self.queue[self.rear]=item
            self.rear=(self.rear+1)%self.size
            self.avabale-=1
    def dequeue(self):
        if self.avabale==self.size:
            print("queue underflow")
            return None
        else:
            item=self.queue[self.front]
            self.queue[self.front]=None
            self.front=(self.front+1)%self.size
            self.avabale+=1
            return item
    def count(self):
        return self.size-self.avabale
    def peek(self):
        return self.queue[self.front]
    
line=queue(5)

line.enqueue("Alice")
line.enqueue("Bob")
line.enqueue("Charlie")
line.enqueue("David")
line.enqueue("Alex")

while line.count()>1:
    for i in range(2):
        item=line.dequeue()
        line.enqueue(item)
    eliminated=line.dequeue()
    print(f"{eliminated} is eliminated")

print(f"The winner is {line.peek()}")