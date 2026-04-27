class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def _connect_circular(self):
        if self.head and self.tail:
            self.tail.next = self.head
            self.head.prev = self.tail

    def __str__(self):
        if not self.head:
            return "List is empty"
        result = []
        current = self.head
        while True:
            result.append(str(current.value))
            current = current.next
            if current == self.head:
                break
        return " <-> ".join(result)

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        self._connect_circular()
        return new_node

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        self._connect_circular()
        return new_node

    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        prev_node = self.get(index - 1)
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node
        self.length += 1
        return new_node

    def traverse(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.value)
            current = current.next
            if current == self.head:
                break

    def reverse_traverse(self):
        if not self.tail:
            print("List is empty")
            return
        current = self.tail
        while True:
            print(current.value)
            current = current.prev
            if current == self.tail:
                break

    def search(self, target):
        if not self.head:
            return False
        current = self.head
        while True:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                return False

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - index - 1):
                current = current.prev
        return current

    def set(self, index, value):
        node = self.get(index)
        node.value = value
        return True

    def pop_first(self):
        if not self.head:
            return None
        popped = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length -= 1
        return popped

    def pop(self):
        if not self.head:
            return None
        popped = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length -= 1
        return popped

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        node = self.get(index)
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1
        return node

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0