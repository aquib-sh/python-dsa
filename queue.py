class Node:
    def __init__(self, value):
        self.value = value
        self.child = None

class Queue:
    def __init__(self):
        self.length = 0
        self._head = None

    def enqueue(self, value):
        if self._head == None: 
            self._head = Node(value)

        else:
            current = self._head
            while (current.child != None):
                current = current.child
            current.child = Node(value)

    def dequeue(self):
        if self._head == None: return
        self._head  = self._head.child

    def __str__(self):
        _str = "{"
        current = self._head
        while current != None:
            _str += f"{current.value},"
            current = current.child
        _str += "}"
        return _str


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    print(queue)

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    print(queue)
