class myStack:
    def __init__(self):
        self.stackList = []
    def push(self, item):
        self.stackList.append(item)
    def pop(self):
        return self.stackList.pop()
    def print(self):
        for i in self.stackList:
            print('[', i, ']', end = ' ')


stack = myStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print()

print()
stack.pop()
stack.print()
