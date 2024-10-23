class myQueue:
    def __init__(self):
        self.queue = []

    def enQueue(self, item):
        self.queue.append(item)

    def deQueue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def print(self):

        print("Queue: ", )
        for i in self.queue:
            print('[', i, ']', end = ' ')

        print()

q = myQueue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)

q.print()

q.deQueue()
q.print()