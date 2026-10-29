class ArrayStack:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: stack is full.")
        self.top = self.top + 1
        self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: stack is empty.")
        value = self.data[self.top]
        self.data[self.top] = None
        self.top = self.top - 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: no top element.")
        return self.data[self.top]

    def show(self):
        return self.data[:self.top + 1]


if __name__ == "__main__":
    stack = ArrayStack(3)
    stack.push("A")
    stack.push("B")
    print("Stack:", stack.show())
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("After pop:", stack.show())
