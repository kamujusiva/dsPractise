# Last in first out

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack_size() < 1:
            return
        data = self.stack[-1]
        print('Deleted ', data, 'from Stack')
        del self.stack[-1]
        return data

    def peek(self):
        if self.stack_size() < 1:
            return
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(8)
print("Stack Size ", stack.stack_size())
stack.pop()
print("Stack Size ", stack.stack_size())
stack.pop()
stack.pop()
stack.pop()
print("Stack Peek", stack.peek())
