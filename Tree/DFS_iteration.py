class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs_iteration(root):
    node_list = [root]
    while len(node_list):
        node = node_list.pop()
        print(node.val)
        if node.right is not None:
            node_list.append(node.right)
        if node.left is not None:
            node_list.append(node.left)


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
    dfs_iteration(root)
