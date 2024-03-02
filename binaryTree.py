"""
Binary Tree
"""

class BinaryTree:
    """
    represents binary tree
    """

    def __init__(self):
        """
        initializes new binary tree
        """
        self.root = None

    def insert_value(self, v):
        """
        insert value v into tree
        :param v:
        :return: the inserted node
        """

        def insert(root, node):
            if root.value == v:
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
        
        if self.root is None:
            self.root = Node(v)
            return self.root
        else:
            return insert(self.root, v)


    def walk_and_print_inorder(self):
        def inorder(node):
            if node.left is not None:
                inorder(node.left)
            print(node.value)
            if node.right is not None:
                inorder(node.right)
        
        inorder(self.root)


    def create_inorder_list(self) -> list:

        def __create_inorder_list(node, list):
            if node.left is not None:
                __create_inorder_list(node.left, list)
            list.append(node.value)
            if node.right is not None:
                __create_inorder_list(node.right, list)

        l = []
        __create_inorder_list(self.root, l)
        return l


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


def main() -> None:
    print('Hello, let\'s build a binary tree')
    print('--------------------------------')

    tree = BinaryTree()

    input_list = (10, 20, 15, 3, 60, 90, 100)
    print(f'input list: {input_list}')
    for value in input_list:
        print(f'insert: {value:3}')
        tree.insert_value(value)
 

    print('All nodes inserted, now lets walk the tree')
    tree.walk_and_print_inorder()

    in_order_list = tree.create_inorder_list()
    print(f'Inorder:  {in_order_list}')


if __name__ == '__main__':
    main()