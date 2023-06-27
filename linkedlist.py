class Node:
    def __init__(self, value=None):
        self.value = value 
        self.child = None

class LinkedList:
    def  __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def first(self):
        return self.head.value;

    def last(self):
        return self.tail.value;

    def add(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            current = self.head
            while current.child != None:
                current = current.child
            current.child = Node(value)
            self.tail = current.child
        self.length += 1

    def addFirst(self, value):
        old_head = self.head
        self.head = Node(value)
        self.head.child = old_head
        self.length += 1

    def pop(self):
        previous = None
        current = self.head
        while current != self.tail:
            previous = current
            current = current.child
        previous.child = None
        self.tail = previous
        self.length -= 1

    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.child
            self.length -= 1
            return True

        current = self.head
        while current.child != None:
            previous = current
            current = current.child

            if (current.value == value):
                previous.child = current.child
                self.length -= 1 
                return True
        return False

    def __str__(self):
        _str = "{"
        current = self.head
        while current != None:
            _str += f"{current.value},"
            current = current.child
        _str += "}"
        return _str

if __name__ == "__main__":
    llist = LinkedList()

    llist.add(10)
    llist.add(20)
    llist.add(30)
    llist.add(40)

    llist.addFirst(60)
    llist.pop()

    print(llist.remove(10))
    print(llist.remove(60))
    print(llist)

