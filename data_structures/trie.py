class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            node = current_node.children.get(char)
            if node is None:
                node = TrieNode()
                current_node.children[char] = node
            current_node = node
        current_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            node = current_node.children.get(char)
            if node is None:
                return False
            current_node = node
        return current_node.is_end_of_word

    def delete(self, word: str) -> bool:
        return self._delete(self.root, word, 0)

    def _delete(self, node: TrieNode, word: str, index: int) -> bool:
        if index == len(word):
            if not node.is_end_of_word:
                return False
            node.is_end_of_word = False
            return len(node.children) == 0
        char = word[index]
        next_node = node.children.get(char)
        if next_node is None:
            return False
        should_delete_child = self._delete(next_node, word, index + 1)
        if should_delete_child:
            del node.children[char]
            return len(node.children) == 0 and not node.is_end_of_word
        return False