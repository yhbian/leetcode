import time
import Tree.PreOrderTraversal as viz


class GenerateTree:
    # TODO: remove empty node
    def __init__(self, string):
        # "1234#567"
        self.string = string
        self.leaves = []
        self._split_tree()
        self._construct_tree()

    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def bfs(self, root):
        node_list = [root]
        while node_list:
            new_list = []
            for node in node_list:
                if node.left is not None:
                    new_list.append(node.left)
                if node.right is not None:
                    new_list.append(node.right)
            if not len(new_list):
                self.leaves = node_list
            node_list = new_list

    def _get_leaves(self, root):
        self.leaves = []
        self.bfs(root=root)

    def _construct_layer(self, layer):
        # convert the string layer into list and '#' to None
        layer_list = []
        for s in layer:
            if s is not '#':
                layer_list.append(int(s))
            else:
                layer_list.append(None)

        # get the leaves and add their children
        self._get_leaves(root=self.root)
        for i, value in enumerate(layer_list):
            if not i % 2:  # even case for left
                self.leaves[int(i/2)].left = self.TreeNode(x=value)
            else:  # odd case for right
                self.leaves[int(i/2)].right = self.TreeNode(x=value)

    def _split_tree(self):
        # This function will split tree into layers
        # "1234#567" -> {0: "1", 1: "23", 2: "4#56", 3: "7#######"} The last layer will be filled automatically
        self.tree_dict = {}
        layer = 0
        while 1:
            start = 2 ** layer - 1
            end = start * 2
            if end+1 < len(self.string):
                self.tree_dict[layer] = self.string[start: end+1]
                layer += 1
            else:
                break
        rest = self.string[start:]
        if rest:
            while len(rest) < 2 ** layer:  # fill the last layer
                rest += '#'
            self.tree_dict[layer] = rest

    def _construct_tree(self):
        if not self.tree_dict:
            self.root = None
            return
        if len(self.tree_dict) == 1:
            if not self.tree_dict[0]:
                self.root = None
            else:
                self.root = self.TreeNode(x=int(self.tree_dict[0]))
            return
        self.root = self.TreeNode(x=int(self.tree_dict[0]))
        for layer in list(self.tree_dict.values())[1:]:
            self._construct_layer(layer=layer)


if __name__ == '__main__':
    s = "12345#67"
    Tree = GenerateTree(string=s)
    root = Tree.root
    viz._pre_order_traversal(root)










