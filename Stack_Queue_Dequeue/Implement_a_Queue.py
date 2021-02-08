class Queue(object):
    def __init__(self):
        self.items = []

    def Enqueue(self, item):
        return self.items.insert(0, item)

    def Dequeue(self):
        return self.items.remove(self.items[0])

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


q = Queue()
# print(q.isEmpty())
q.Enqueue(1)
print(q.isEmpty())
print(q.size())
q.Enqueue("hello")