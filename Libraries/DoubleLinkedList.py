from Libraries.Node import Node

'''
This is a double linked list

-1 default value for use in question First Unique Number
'''


class DoubleLinkedList:

    def __init__(self, default_val):
        self.head = Node(default_val)
        self.tail = Node(default_val)
        self.head.next, self.tail.prev = self.tail, self.head
        self.length = 0

    def remove_node(self, node):
        prevn, nextn = node.prev, node.next
        node.prev.next = nextn
        node.next.prev = prevn
        self.length -= 1

    def add_node(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.length += 1
