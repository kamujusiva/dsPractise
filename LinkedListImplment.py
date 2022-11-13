class Node:
    def __int__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.no_of_nodes = None
        self.head = None

    def insert_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.no_of_nodes = self.no_of_nodes + 1

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            traversal_node = self.head
            while traversal_node.next_node is not None:
                traversal_node = traversal_node.next_node
            traversal_node.next_node = new_node

    def traverse(self):
        traversal_node = self.head
        while traversal_node.next_node is not None:
            print(traversal_node)
            traversal_node = traversal_node.next_node

    def remove_item(self, data):
        pass


linked_list = LinkedList()
linked_list.insert_start(10)
linked_list.insert_start(20)
linked_list.insert_end('Adam')
linked_list.insert_end('4.5')
linked_list.traverse()