# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem


def print_linked_list(head):
    """
    Print all elements recursively until the all heads are exhausted
    """
    if head:
        print(head.data)
        print_linked_list(head.next)
