class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bfs_iteration(root):
    node_list = [root]
    while len(node_list):
        new_list = []
        for node in node_list:
            if node.left is not None:
                new_list.append(node.left)
            if node.right is not None:
                new_list.append(node.right)
        node_list = new_list


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
    bfs_iteration(root)
