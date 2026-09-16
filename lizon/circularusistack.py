class CircularQueueUsingStack:
    def __init__(self, size):
        self.size = size
        self.stack = []
    def enqueue(self, value):
        if len(self.stack) == self.size:
            print("Queue is full")
            return
        self.stack.append(value)
    def dequeue(self):
        if len(self.stack) == 0:
            print("Queue is empty")
            return
        # First element বের করার জন্য
        temp = []
        while len(self.stack) > 1:
            temp.append(self.stack.pop())
        value = self.stack.pop()
        while len(temp) > 0:
            self.stack.append(temp.pop())
        return value
    def display(self):
        print(self.stack)
cq = CircularQueueUsingStack(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()
print("Deleted:", cq.dequeue())
cq.display()