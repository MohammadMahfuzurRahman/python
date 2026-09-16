class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return
        value = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return value
    def display(self):
        print(self.queue)
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()
print("Deleted:", cq.dequeue())
cq.display()