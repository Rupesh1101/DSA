class Queue(object):

    def __init__(self):
        self.instack = []
        self.outstack = []
    
    def enqueue(self,item):
        self.instack.append(item)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())