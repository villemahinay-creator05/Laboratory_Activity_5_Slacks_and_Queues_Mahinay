class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        # A linked stack has no fixed capacity.
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: stack is empty.")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: no top element.")
        return self.top.value

    def show(self):
        values = []
        current = self.top
        while current is not None:
            values.append(current.value)
            current = current.next
        return values


if __name__ == "__main__":
    stack = LinkedStack()
    stack.push("A")
    stack.push("B")
    print("Stack (top to bottom):", stack.show())
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("After pop:", stack.show())
