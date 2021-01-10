import time


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def _visualize_link(pHead):
    if pHead is not None:
        print(pHead.val)
        return _visualize_link(pHead.next)
    else:
        return


if __name__ == '__main__':
    lst = [1, 2, 3]
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    pHead = node1

    _visualize_link(pHead)
