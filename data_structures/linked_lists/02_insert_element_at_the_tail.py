# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

from .linked_list_common import Node


def insert(head, data):
    """
    Recursive insert if there is head, otherwise initialize the head with the given data
    """
    if head:
        head.next = insert(head.next, data)
    else:
        head = Node(data)
    return head
