class Node:
    def __init__(self, value):
        self.value = value
        self.child = None

class Stack:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def push(self, value):
        if self._head == None:
            self._head = Node(value)
            self._tail = self._head

        else:
            current = self._head
            while current.child != None:
                current = current.child

            current.child = Node(value)
            self._tail = current.child

        self._length += 1

    def peek(self):
        return self._tail.value

    def pop(self):
        if self._head == None: return

        if self._head.child == None:
            value = self._head.value
            self._head = None
            return value

        current = self._head
        previous = None

        while current.child != None:
            previous = current
            current = current.child

        previous.child = None
        return current.value

    def length(self): 
        return self._length;


    def __str__(self):
        _str = "{"
        current = self._head
        while current != None:
            _str += f"{current.value},"
            current = current.child
        _str += "}"
        return _str


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    
    print(stack)
    print("last value is ", stack.peek())

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    print(stack)


