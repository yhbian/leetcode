import time


def _visualize_tree(root):
    if root is not None:
        print(root.val)
        _visualize_tree(root.left)
        _visualize_tree(root.right)
        return
