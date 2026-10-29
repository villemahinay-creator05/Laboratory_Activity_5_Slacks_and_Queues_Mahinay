class ArrayQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.data)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow: queue is full.")
        rear = (self.front + self.size) % len(self.data)
        self.data[rear] = value
        self.size = self.size + 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: queue is empty.")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size = self.size - 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: no front element.")
        return self.data[self.front]

    def show(self):
        values = []
        for i in range(self.size):
            index = (self.front + i) % len(self.data)
            values.append(self.data[index])
        return values


if __name__ == "__main__":
    queue = ArrayQueue(3)
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    print("Queue:", queue.show())
    print("Dequeue:", queue.dequeue())
    queue.enqueue("D")  # demonstrates circular wrap-around
    print("After wrap-around:", queue.show())
