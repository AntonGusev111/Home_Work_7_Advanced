class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self,value):
       self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            return 'stak is empty'
        else:
            self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return 'stak is empty'
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)




