"""
July 10 Challenge - Flatten a Multilevel Doubly Linked List

Diagram: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer,
which may or may not point to a separate doubly linked list.

These child lists may have one or more children of their own, and so on, to produce a multilevel data structure,
as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list.
You are given the head of the first level of the list.
"""


def flatten(head):
    """
    :type head: Node
    :rtype: Node
    """
    temp = head
    stack = []

    while temp:
        if temp.child:
            if temp.next:
                stack.append(temp.next)
            temp.next = temp.child
            temp.child.prev = temp
            temp.child = None
            temp = temp.next

        elif temp.next:
            temp = temp.next

        elif stack:
            pop_node = stack.pop()
            temp.next = pop_node
            pop_node.prev = temp
            temp = temp.next
        else:
            temp.next = None
            temp = temp.next

    return head
