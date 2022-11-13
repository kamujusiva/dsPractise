class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:

    def __init__(self):
        self.no_of_nodes = 0
        self.head_node = None
        self.tail_node = None

    def size_of_linkedlist(self):
        return self.no_of_nodes

    def insert_end(self, data):
        new_node = Node(data)
        if self.head_node is None:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            new_node.previous_node = self.tail_node
            self.tail_node.next_node = new_node
            self.tail_node = new_node

    def traverse_forward(self):
        print("==========================================")
        print("Traversing Forward")
        print("==========================================")
        traversal_node = self.head_node
        while traversal_node.next_node is not None:
            print(traversal_node.data, '\t Previous ', traversal_node.previous_node, '\tNext Node '
                  , traversal_node.next_node)
            traversal_node = traversal_node.next_node
        print(traversal_node.data, '\t Previous ', traversal_node.previous_node, '\tNext Node '
              , traversal_node.next_node)

    def traverse_backward(self):
        print("==========================================")
        print("Traversing Backward")
        print("==========================================")
        traversal_node = self.tail_node
        while traversal_node.previous_node is not None:
            print(traversal_node.data, '\t Previous ', traversal_node.previous_node, '\tNext Node '
                  , traversal_node.next_node)
            traversal_node = traversal_node.previous_node
        print(traversal_node.data, '\t Previous ', traversal_node.previous_node, '\tNext Node '
              , traversal_node.next_node)

dll_list = DoublyLinkedList()
dll_list.insert_end(2)
dll_list.insert_end(3)
dll_list.insert_end(6)
dll_list.insert_end(5)
dll_list.traverse_forward()
dll_list.traverse_backward()