class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def _construct_link(lst):
    r"""
    :param lst: [1, 2, 3, 4], a list
    :return: 1 -> 2 -> 3 -> 4 -> None
    """
    # empty LinkList
    if not lst:
        return None
    if len(lst) == 1:
        return ListNode(lst[0])

    node, next_node = None, ListNode(lst[-1])
    for i in range(1, len(lst)):
        # construct the LinkList from tail to head
        node = ListNode(lst[-i-1])
        node.next = next_node
        next_node = node

    return node
