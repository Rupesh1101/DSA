class DoublyLinkedList(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None
        self.previousNode = None

a = DoublyLinkedList(1)
b = DoublyLinkedList(2)
c = DoublyLinkedList(3)

a.nextNode = b
b.previousNode = a

b.nextNode = c
c.previousNode = b

print(a.value)
print(a.nextNode.value)

print(b.value)
print(b.previousNode.value)

print(b.value)
print(b.nextNode.value)