class CircularQueueUsingQueue:

    def __init__(self, size):
        self.size = size
        self.queue = []
    def enqueue(self, value):
        if len(self.queue) == self.size:
            print("Queue is full")
            return
        self.queue.append(value)
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return
        value = self.queue.pop(0)
        return value
    def display(self):
        print(self.queue)
cq = CircularQueueUsingQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()
print("Deleted:", cq.dequeue())
cq.display()