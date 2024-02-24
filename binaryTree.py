"""
Binary Tree
"""


class Node:
    """
    represents a node of the tree
    """
    def __init__(self, v=None):
        """
        create a new node
        :param v:
        """
        self.value = v
        self.left = None
        self.right = None


def insert(root, v):
    """
    insert value v into tree
    :param root:
    :param v:
    :return: the inserted node
    """
    if root is None:
        return Node(v)
    elif root.value == v:
        return root
    elif root.value > v:
        if root.left is None:
            root.left = Node(v)
            return root.left
        else:
            insert(root.left, v)
    elif root.value < v:
        if root.right is None:
            root.right = Node(v)
            return root.right
        else:
            insert(root.right, v)


def walk_and_print_inorder(node):
    """

    :param node:
    :return:
    """
    if node.left is not None:
        walk_and_print_inorder(node.left)
    print(node.value)
    if node.right is not None:
        walk_and_print_inorder(node.right)


def create_inorder_ist(node, list):
    """

    :param node:
    :return:
    """
    if node.left is not None:
        create_inorder_ist(node.left, list)
    list.append(node.value)
    if node.right is not None:
        create_inorder_ist(node.right, list)



def demo():
    print('Hello, lets build a binary tree')
    print('-------------------------------')

    tree = None

    input_list = (10, 20, 15, 3, 60, 90, 100)

    for value in input_list:
        print(f'insert: {value:3}')
        node = insert(tree, value)
        if tree is None:
            tree = node

    print("All nodes inserted, now lets walk the tree")
    walk_and_print_inorder(tree)

    l = []
    create_inorder_ist(tree, l)

    print(l)



if __name__ == '__main__':
    demo()