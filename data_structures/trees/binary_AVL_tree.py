from collections import deque

class AVLTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 1

    def preorder_traversal(self, i=0):
        print(' ' * i + str(self.value))
        if self.left_child:
            self.left_child.preorder_traversal(i + 1)
        if self.right_child:
            self.right_child.preorder_traversal(i + 1)

    def inorder_traversal(self, i=0):
        if self.left_child:
            self.left_child.inorder_traversal(i + 1)
        print(' ' * i + str(self.value))
        if self.right_child:
            self.right_child.inorder_traversal(i + 1)

    def postorder_traversal(self, i=0):
        if self.left_child:
            self.left_child.postorder_traversal(i + 1)
        if self.right_child:
            self.right_child.postorder_traversal(i + 1)
        print(' ' * i + str(self.value))

    def levelorder_traversal(self):
        queue = deque([self])
        while queue:
            node = queue.popleft()
            print(node.value)
            if node.left_child:
                queue.append(node.left_child)
            if node.right_child:
                queue.append(node.right_child)

    def get_balance(self):
        return get_height(self.left_child) - get_height(self.right_child)

    def minimum_node(self):
        current = self
        while current.left_child:
            current = current.left_child
        return current

def get_height(node):
    if node is None:
        return 0
    return node.height

def right_rotation(z):
    y = z.left_child
    T3 = y.right_child
    y.right_child = z
    z.left_child = T3
    z.height = 1 + max(get_height(z.left_child), get_height(z.right_child))
    y.height = 1 + max(get_height(y.left_child), get_height(y.right_child))
    return y

def left_rotation(z):
    y = z.right_child
    T2 = y.left_child
    y.left_child = z
    z.right_child = T2
    z.height = 1 + max(get_height(z.left_child), get_height(z.right_child))
    y.height = 1 + max(get_height(y.left_child), get_height(y.right_child))
    return y

def insertNode(avl_tree, value):
    if avl_tree is None:
        return AVLTree(value)
    if value < avl_tree.value:
        avl_tree.left_child = insertNode(avl_tree.left_child, value)
    else:
        avl_tree.right_child = insertNode(avl_tree.right_child, value)
    avl_tree.height = 1 + max(get_height(avl_tree.left_child), get_height(avl_tree.right_child))
    balance = avl_tree.get_balance()
    if balance > 1:
        if value < avl_tree.left_child.value:
            return right_rotation(avl_tree)
        else:
            avl_tree.left_child = left_rotation(avl_tree.left_child)
            return right_rotation(avl_tree)
    if balance < -1:
        if value > avl_tree.right_child.value:
            return left_rotation(avl_tree)
        else:
            avl_tree.right_child = right_rotation(avl_tree.right_child)
            return left_rotation(avl_tree)
    return avl_tree

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
    root.height = 1 + max(get_height(root.left_child), get_height(root.right_child))
    balance = root.get_balance()
    if balance > 1:
        if root.left_child.get_balance() >= 0:
            return right_rotation(root)
        else:
            root.left_child = left_rotation(root.left_child)
            return right_rotation(root)
    if balance < -1:
        if root.right_child.get_balance() <= 0:
            return left_rotation(root)
        else:
            root.right_child = right_rotation(root.right_child)
            return left_rotation(root)
    return root

def delete_entire_tree(root):
    return None