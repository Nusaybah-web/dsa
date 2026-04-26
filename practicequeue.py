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
    def peek(self):
        print(self.queue[self.front])
    def getrear(self):
        print(self.queue[self.rear])
    def printqueue(self):
        print(self.queue)
    def isempty(self):
        return self.avabale==self.size


"""line=["Alice", "Bob", "Charlie"]

line.append("David")
while line:
    person=line.pop(0)
    print(person+" bought a ticket")

print(line)"""

line=queue(5)

line.enqueue("Alice")
line.enqueue("Bob")
line.enqueue("Charlie")
line.enqueue("David")

while not line.isempty():
    person=line.dequeue()
    print(person+" bought a ticket")
