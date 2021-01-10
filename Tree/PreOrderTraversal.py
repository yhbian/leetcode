class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def _pre_order_traversal(root):
    if root is not None:
        print(root.val)
        _pre_order_traversal(root.left)
        _pre_order_traversal(root.right)
        return


if __name__ == '__main__':
    # define Tree
    leaf1 = TreeNode(5)
    leaf2 = TreeNode(7)
    leaf3 = TreeNode(9)
    leaf4 = TreeNode(11)
    left_branch = TreeNode(6)
    left_branch.left = leaf1
    left_branch.right = leaf2
    right_branch = TreeNode(10)
    right_branch.left = leaf3
    right_branch.right = leaf4
    root = TreeNode(8)
    root.left = left_branch
    root.right = right_branch

    # test code
    _pre_order_traversal(root)
