class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        # A linked queue has no fixed capacity.
        return False

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: queue is empty.")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: no front element.")
        return self.front.value

    def show(self):
        values = []
        current = self.front
        while current is not None:
            values.append(current.value)
            current = current.next
        return values


if __name__ == "__main__":
    queue = LinkedQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    print("Queue (front to rear):", queue.show())
    print("Dequeue:", queue.dequeue())
    print("After dequeue:", queue.show())
