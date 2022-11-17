class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left_node = None
        self.right_node = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, current_node):
        if data < current_node.data:
            if current_node.left_node is not None:
                self.insert_node(data, current_node.left_node)
            else:
                current_node.left_node = Node(data, parent=current_node)
        elif data > current_node.data:
            if current_node.right_node is not None:
                self.insert_node(data, current_node.right_node)
            else:
                current_node.right_node = Node(data, parent=current_node)
        else:
            return

    def get_min(self):
        if self.root is None:
            return None
        else:
            self.get_min_value(self.root)

    def get_min_value(self, current_node):
        if current_node.left_node is not None:
            self.get_min_value(current_node.left_node)
        return current_node.data

    def get_max(self):
        if self.root is not None:
            self.get_max_value(self.root)

    def get_max_value(self, current_node):
        if current_node.right_node is not None:
            self.get_max_value(current_node.right_node)
        return current_node.data

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, current_node):
        if current_node.left_node is not None:
            self.traverse_in_order(current_node.left_node)
        print(current_node.data)
        if current_node.right_node is not None:
            self.traverse_in_order(current_node.right_node)

bst = BinarySearchTree()
import  random
for i in range(1, 40):
    bst.insert_node(random.randint(1, 16))
bst.traverse()








