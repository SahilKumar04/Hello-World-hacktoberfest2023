class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

# Creating a queue
my_queue = Queue()

# Enqueueing elements
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

# Dequeueing elements
dequeued_item = my_queue.dequeue()
print("Dequeued item:", dequeued_item)  # Should print 1

# Checking the size of the queue
queue_size = my_queue.size()
print("Queue size:", queue_size)  # Should print 2
