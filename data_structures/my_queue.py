from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def __str__(self):
        return "->".join(str(x) for x in self.items)

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def enqueue(self, item) -> None:
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def delete(self) -> None:
        self.items.clear()