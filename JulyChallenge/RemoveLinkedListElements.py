from Libraries.Node import Node

"""
July 20 Challenge - Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""


def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    pre_head = Node(-1, head)
    curr = pre_head

    while curr and curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return pre_head.next
