class Node(object):
    """二叉树节点"""

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class MyBinaryTree(object):
    """二叉树极其先、中、后序遍历的递归实现"""

    def __init__(self, node=None):
        self.head = node

    def pre_traversal(self, start: Node):
        """先序遍历的递归实现"""

        if start:
            print(start.val)
            self.pre_traversal(start.left)
            self.pre_traversal(start.right)

    def in_traversal(self, start: Node):
        """中序遍历的递归实现"""

        if start:
            self.in_traversal(start.left)
            print(start.val)
            self.in_traversal(start.right)

    def pos_traversal(self, start: Node):
        """后序遍历的递归实现"""

        if start:
            self.pos_traversal(start.left)
            self.pos_traversal(start.right)
            print(start.val)


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    my_bt = MyBinaryTree(n1)
    print('先序遍历：')
    my_bt.pre_traversal(my_bt.head)
    print('中序遍历：')
    my_bt.in_traversal(my_bt.head)
    print('后序遍历：')
    my_bt.pos_traversal(my_bt.head)
