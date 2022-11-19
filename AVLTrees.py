class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left_node = None
        self.right_node = None
        self.height = 0


class AVLTree:
    def __init__(self):
        # we can access root node exclusively
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, current_node: Node):
        if data < current_node.data:
            if current_node.left_node is not None:
                self.insert_node(data, current_node.left_node)
            else:
                current_node.left_node = Node(data, parent=current_node)
                current_node.height = max(self.calc_height(current_node.left_node),
                                          self.calc_height(current_node.right_node))+1
        elif data > current_node.data:
            if current_node.right_node is not None:
                self.insert_node(data, current_node.right_node)
            else:
                current_node.right_node = Node(data, parent=current_node)
                current_node.height = max(self.calc_height(current_node.left_node),
                                          self.calc_height(current_node.right_node)) + 1
        else:
            return
        # After every insertion check for balance of AVL Tree
        self.handle_balance(current_node)

    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)

    def remove_node(self, data, current_node):
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
                self.handle_balance(parent)
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
                self.handle_balance(parent)
            # if there is single left child
            elif current_node.left_node is not None and current_node.right_node is None:
                print("Removing the node with single left child: ", current_node.data)
                parent = current_node.parent
                if parent is not None and parent.left_node == current_node:
                    parent.left_node = current_node.left_node
                elif parent is not None and parent.right_node == current_node:
                    parent.right_node = current_node.left_node
                else:
                    self.root = current_node.left_node
                current_node.left_node_node.parent = parent
                del current_node
                self.handle_balance(parent)
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

    def calc_height(self, given_node: Node):
        if given_node is None:
             return -1


    def handle_balance(self, given_node: Node):
        pass
