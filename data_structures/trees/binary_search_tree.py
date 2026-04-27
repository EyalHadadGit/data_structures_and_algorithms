from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert(self, value):
        root = self
        while True:
            if value < root.value:
                if root.left_child is None:
                    root.left_child = BSTNode(value)
                    return
                root = root.left_child
            else:
                if root.right_child is None:
                    root.right_child = BSTNode(value)
                    return
                root = root.right_child

    def preorder_traversal(self, depth=0):
        print(' ' * depth + str(self.value))
        if self.left_child:
            self.left_child.preorder_traversal(depth + 1)
        if self.right_child:
            self.right_child.preorder_traversal(depth + 1)

    def inorder_traversal(self, depth=0):
        if self.left_child:
            self.left_child.inorder_traversal(depth + 1)
        print(' ' * depth + str(self.value))
        if self.right_child:
            self.right_child.inorder_traversal(depth + 1)

    def postorder_traversal(self, depth=0):
        if self.left_child:
            self.left_child.postorder_traversal(depth + 1)
        if self.right_child:
            self.right_child.postorder_traversal(depth + 1)
        print(' ' * depth + str(self.value))

    def level_order_traversal(self):
        queue = deque()
        queue.append(self)
        while queue:
            node = queue.popleft()
            print(node.value)
            if node.left_child:
                queue.append(node.left_child)
            if node.right_child:
                queue.append(node.right_child)

    def search(self, data):
        if self.value == data:
            return True
        child = self.left_child if data < self.value else self.right_child
        if child:
            return child.search(data)
        return False

    def minimum_node(self):
        current = self
        while current.left_child:
            current = current.left_child
        return current

def delete_node(root, value):
    if root is None:
        return None
    if value < root.value:
        root.left_child = delete_node(root.left_child, value)
    elif value > root.value:
        root.right_child = delete_node(root.right_child, value)
    else:
        if root.left_child is None:
            return root.right_child
        if root.right_child is None:
            return root.left_child
        successor = root.right_child.minimum_node()
        root.value = successor.value
        root.right_child = delete_node(root.right_child, successor.value)
    return root


def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if not node:
        return True

    if not (min_val < node.value < max_val):
        return False

    return (
        is_bst(node.left_child, min_val, node.value) and
        is_bst(node.right_child, node.value, max_val)
    )