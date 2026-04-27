class BSTNode:
    def __init__(self, data=None, left = None, right= None):
        self.data = data
        self.left = left
        self.right = right

def minimal_tree(sorted_array):
    if not sorted_array:
        return None
    mid = len(sorted_array) // 2
    return BSTNode(
        sorted_array[mid],
        minimal_tree(sorted_array[:mid]),
        minimal_tree(sorted_array[mid + 1:])
    )

def preorder_traversal(root):
    result = []
    def dfs(node):
        if not node:
            return
        result.append(node.data)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return result