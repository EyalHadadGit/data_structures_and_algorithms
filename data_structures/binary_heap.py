class BinaryHeap:
    # Array-based Binary Heap supporting Min and Max configurations.
    # Operations:
    # - insert: O(log n)
    # - extract_root: O(log n)
    # - peek: O(1)

    def __init__(self, capacity: int, heaptype: str = 'Max'):
        # Initialize the heap.

        # :param capacity: Maximum number of elements
        # :param heaptype: 'Min' or 'Max'

        if heaptype not in ('Min', 'Max'):
            raise ValueError("heaptype must be 'Min' or 'Max'")
        self.heap = [None] * (capacity + 1)
        self.size = 0
        self.capacity = capacity
        self.heaptype = heaptype

    def _should_swap_up(self, child, parent):
        if self.heaptype == 'Min':
            return child < parent
        return child > parent

    def _should_swap_down(self, parent, child):
        if self.heaptype == 'Min':
            return parent > child
        return parent < child

    def peek(self):
        if self.size == 0:
            raise Exception("Heap is empty")
        return self.heap[1]

    def level_order(self):
        return self.heap[1:self.size + 1]

    def insert(self, value):
        if self.size >= self.capacity:
            raise Exception('Heap Overflow')
        index = self.size + 1
        while index >= 2:
            parent = index // 2
            if not self._should_swap_up(value, self.heap[parent]):
                break
            self.heap[index] = self.heap[parent]
            index = parent
        self.heap[index] = value
        self.size += 1

    def extract_root(self):
        if self.size == 0:
            raise Exception("Heap is empty")
        root = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = None
        self.size -= 1
        index = 1
        while index * 2 <= self.size:
            left = index * 2
            right = left + 1
            if right <= self.size:
                if self._should_swap_down(self.heap[left], self.heap[right]):
                    chosen = right
                else:
                    chosen = left
            else:
                chosen = left
            if not self._should_swap_down(self.heap[index], self.heap[chosen]):
                break
            self.heap[index], self.heap[chosen] = self.heap[chosen], self.heap[index]
            index = chosen
        return root

    def clear(self):
        self.heap = [None] * (self.capacity + 1)
        self.size = 0

    def __str__(self):
        return str(self.level_order())