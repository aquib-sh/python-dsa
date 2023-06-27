class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def addFirst(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def addLast(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = self.head

        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def remove(self, value):
        if value == self.head.value:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return True
        
        current = self.head
        while (current != None):
            current = current.next

            if current.value == value:
                current.prev.next = current.next
                self.length -= 1
                return True
        return False

    def removeFirst(self):
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1

    def removeLast(self):
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1

    def __str__(self):
        current = self.head
        _str = "{"
        while (current != None):
            _str += f"{current.value},"
            current = current.next
        _str += "}"
        return _str


if __name__ == "__main__":
    _list = DoublyLinkedList()
    _list.addLast(10)
    _list.addLast(20)
    _list.addLast(30)
    _list.addLast(40)
    _list.addLast(50)


    _list.addFirst(-50)
    _list.addFirst(-60)
    _list.addFirst(-70)


    _list.remove(-60)
    _list.removeFirst()
    _list.removeLast()

    print(_list)

