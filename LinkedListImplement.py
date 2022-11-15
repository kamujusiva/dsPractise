class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.no_of_nodes = 0
        self.head = None

    def size_of_linkedlist(self):
        return self.no_of_nodes

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
        self.no_of_nodes = self.no_of_nodes + 1

    def traverse(self):
        print("Current Linked List Contains ", self.no_of_nodes, 'entries')
        traversal_node = self.head
        while traversal_node.next_node is not None:
            print("Value at Current Node:\t", traversal_node.data, '\t\tAddress is ', traversal_node
                  , '\tNext Node Address', traversal_node.next_node)
            traversal_node = traversal_node.next_node
        print("Value at Current Node:\t", traversal_node.data, '\t\tAddress is ', traversal_node, '\tNext Node Address'
              , traversal_node.next_node)

    def remove_item(self, data):
        if self.head is None:
            return
        traversal_node = self.head
        previous_node = None
        if self.head.data == data:
            self.head = self.head.next_node
            return
        while traversal_node.next_node is not None:
            if traversal_node.data == data:
                previous_node.next_node = traversal_node.next_node
                return
            previous_node = traversal_node
            traversal_node = traversal_node.next_node
        if traversal_node.data == data:
            previous_node.next_node = None
            return
        return

    def reverse_linked_list(self):
        traversal_node = self.head
        while traversal_node.next_node is not None:
            next_node = traversal_node.next_node



linked_list = LinkedList()
linked_list.insert_start(10)
linked_list.insert_start(20)
linked_list.insert_end('Adam')
linked_list.insert_end(4.5)
linked_list.insert_end('456')
linked_list.insert_end(60)
linked_list.insert_end(70)
linked_list.insert_end(90)
linked_list.traverse()
print('=================')
linked_list.remove_item(1000)
linked_list.remove_item(4.5)
linked_list.traverse()
