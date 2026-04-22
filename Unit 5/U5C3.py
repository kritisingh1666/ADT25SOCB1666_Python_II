from collections import deque

# Queue implementation
class Queue:
    def __init__(self):
        self.queue = deque()

    # Enqueue operation
    def enqueue(self, item):
        self.queue.append(item)
        print(item, "added to queue")

    # Safe dequeue operation
    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty, cannot dequeue.")
        else:
            return self.queue.popleft()

    # Display queue
    def display(self):
        print("Queue:", list(self.queue))


# Main program
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Dequeued element:", q.safe_dequeue())
print("Dequeued element:", q.safe_dequeue())
print("Dequeued element:", q.safe_dequeue())

# Trying to dequeue from empty queue
print("Dequeued element:", q.safe_dequeue())
