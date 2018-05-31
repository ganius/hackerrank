# https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
from .linked_list_common import Node


def insert(head, data):
    """
    Since the data is another Node, simply setting it as the data of a new Node means inserting at the head.
    :param head: head to be inserted
    :param data: Node object
    :return: Node object
    """
    return Node(data, head)
