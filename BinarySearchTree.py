import random


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
            return self.get_min_value(self.root)

    def get_min_value(self, current_node):
        if current_node.left_node is not None:
            return self.get_min_value(current_node.left_node)
        return current_node.data

    def get_max(self):
        if self.root is not None:
            return self.get_max_value(self.root)

    def get_max_value(self, current_node):
        if current_node.right_node is not None:
            return self.get_max_value(current_node.right_node)
        return current_node.data

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, current_node):
        if current_node.left_node is not None:
            self.traverse_in_order(current_node.left_node)
        print(current_node.data, end=' ')
        if current_node.right_node is not None:
            self.traverse_in_order(current_node.right_node)

    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)

    def remove_node(self, data, current_node: Node):
        # First we have to find the node to remove
        if current_node is None:
            return
        elif data < current_node.data:
            self.remove_node(data, current_node.left_node)
        elif data > current_node.data:
            self.remove_node(data, current_node.right_node)
        else:
            # we found the node to remove
            # we have 3 options
            # 1. node can be leaf node. this is easy
            if current_node.left_node is None and current_node.right_node is None:
                print("Removing Leaf Node: ", current_node.data)
                parent = current_node.parent
                if parent is not None and parent.left_node == current_node:
                    parent.left_node = None
                elif parent is not None and parent.right_node == current_node:
                    parent.right_node = None
                else:
                    self.root = None
                del current_node
            # if there is a single right child
            elif current_node.left_node is None and current_node.right_node is not None:
                print("Removing the node with single right child: ", current_node.data)
                parent = current_node.parent
                if parent is not None and parent.left_node == current_node:
                    parent.left_node = current_node.right_node
                elif parent is not None and parent.right_node == current_node:
                    parent.right_node = current_node.right_node
                else:
                    self.root = current_node.right_node
                current_node.right_node.parent = parent
                del current_node
            # if there is single left child
            elif current_node.left_node is not None and current_node.right_node is None:
                print("Removing the node with single right child: ", current_node.data)
                parent = current_node.parent
                if parent is not None and parent.left_node == current_node:
                    parent.left_node = current_node.left_node
                elif parent is not None and parent.right_node == current_node:
                    parent.right_node = current_node.left_node
                else:
                    self.root = current_node.left_node
                current_node.left_node_node.parent = parent
                del current_node
            # Removing node with 2 children
            else:
                print("Removing node with 2 children: ", current_node.data)
                predecessor = self.get_predecessor(current_node.left_node)
                # Swap the current_node with predecessor
                temp = predecessor.data
                predecessor.data = current_node.data
                current_node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, current_node: Node):
        if current_node.right_node is not None:
            return self.get_predecessor(current_node.left_node)
        return current_node


bst = BinarySearchTree()
for i in range(1, 40):
    bst.insert(random.randint(1, 15))
print("Minimum Value in Tree is:\t", bst.get_min())
print("Maximum Value in Tree is:\t", bst.get_max())
bst.traverse()
