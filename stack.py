class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == False

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
