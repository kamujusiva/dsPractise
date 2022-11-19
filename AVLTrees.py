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
                                          self.calc_height(current_node.right_node)) + 1
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

    def handle_balance(self, given_node: Node):
        # check the nodes from given node we have inserted up to the root node
        while given_node is not None:
            given_node.height = max(self.calc_height(given_node.left_node),
                                    self.calc_height(given_node.right_node)) + 1
            self.balance_helper(given_node)
            # whenever we fix an imbalance situation, it may happen that,
            # it could cause imbalance in other parts of the tree
            given_node = given_node.parent

    # Check whether the subtree is balanced with root node = given_node
    def balance_helper(self, given_node: Node):
        balance = self.balance_factor(given_node)
        # This is left heavy situation. But it can be left-right heavy or left-left heavy
        if balance > 1:
            # Now check for left right heavy situation: left rotation on parent + right rotation on grandparent
            if self.balance_factor(given_node.left_node) < 0:
                self.rotate_left(given_node.left_node)
            # This is right rotation on grandparent
            self.rotate_right(given_node)

        # This is right heavy situation. But it can be right-left heavy or right-right heavy
        if balance < -1:
            # Now check for right left heavy situation: right rotation on parent + left rotation on grandparent
            if self.balance_factor(given_node.right_node) > 0:
                self.rotate_right(given_node.right_node)
            # This is right rotation on grandparent
            self.rotate_left(given_node)


    def calc_height(self, given_node: Node):
        if given_node is None:
            return -1
        return given_node.height

    def balance_factor(self, given_node: Node):
        if given_node is None:
            return 0

        return (self.calc_height(given_node.left_node) - self.calc_height(given_node.right_node))


