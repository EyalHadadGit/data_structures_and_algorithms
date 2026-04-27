class Stack:
    def __init__(self) -> None:
        self._items = []

    def __str__(self) -> str:
        if not self._items:
            return "Stack is empty"
        return "Stack (top → bottom):\n" + "\n".join(reversed(self._items))

    def push(self, item) -> None:
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def size(self) -> int:
        return len(self._items)

    def clear(self) -> None:
        self._items = []

    def __len__(self) -> int:
        return len(self._items)