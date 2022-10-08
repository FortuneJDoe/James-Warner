class Node(object):
    """二叉树节点"""

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class UnrecursiveBinaryTree(object):
    """二叉树极其先、中、后序遍历的非递归实现"""

    def __init__(self, node=None):
        self.head = node

    def pre_traversal(self, start: Node):
        """先序遍历的非递归实现"""

        print('pre-order:')
        if start:
            stack = list()  # 准备一个空栈
            stack.append(start)  # 将当前节点压入栈内
            while stack:  # 只要栈不为空
                start = stack.pop()  # 弹出栈顶节点，同时start指针指向被弹出节点
                print(start.val, end=' ')  # 打印被弹出节点的元素值
                if start.right:  # 先看右侧，如果右指针不为空
                    stack.append(start.right)  # 右子节点压入栈
                if start.left:  # 然后看左侧，如果左指针不为空
                    stack.append(start.left)  # 左子节点压入栈
        print('\n')

    def in_traversal(self, start: Node):
        """中序遍历的非递归实现(核心思想，优先压入左边界)"""

        print('in-order:')
        if start:  # start指针不指向空
            stack = list()  # 准备空栈
            while stack or start:  # 当栈或start指向位置不全为空时
                if start:  # 如果start指向位置不为空
                    stack.append(start)  # 节点压入栈
                    start = start.left  # start指针来到节点的左子节点位置
                else:  # 如果栈不为空但当前start指向位置为空
                    start = stack.pop()  # 栈顶节点弹出，且start指针指向被弹出节点(不可以理解成回到父节点，反例:当start.right is None时)
                    print(start.val, end=' ')  # 打印被弹出节点的值
                    start = start.right  # start指针来到被弹出节点的右子节点
        print('\n')

    def pos_traversal(self, start: Node):
        """后序遍历的非递归实现"""

        print('pos-order:')
        if start:
            stack_hidding = list()  # 准备一个空栈，作为隐藏栈
            stack_hidding.append(start)  # 将当前节点压入隐藏栈内
            stack_output = list()  # 准备另一个空栈，作为输出栈
            while stack_hidding:  # 只要栈不为空
                start = stack_hidding.pop()  # 弹出隐藏栈顶节点，同时start指针指向被弹出节点
                stack_output.append(start.val)  # 被弹出节点的元素压入输出栈中
                if start.left:  # 先看左侧，如果左指针不为空
                    stack_hidding.append(start.left)  # 左子节点压入隐藏栈
                if start.right:  # 然后看右侧，如果右指针不为空
                    stack_hidding.append(start.right)  # 右子节点压入隐藏栈
            # P.S. 输出栈的压栈顺序：头→右→左。那么输出顺序就是左→右→头，满足后序遍历要求
            while stack_output:  # 只要输出栈中有剩余元素
                print(stack_output.pop(), end=' ')  # 打印栈顶元素
        print('\n')

    def advanced_pos_traversal(self, start: Node):
        """单栈双指针实现非递归后序遍历"""

        print('pos-order advanced:')
        if start:  # start指针不指向空
            stack = list()  # 准备一个空栈
            stack.append(start)  # 将起始节点压入栈中
            tracing = start  # 跟踪指针，跟踪上一个打印元素的节点。初始指向start
            while stack:  # 栈不为空
                current = stack[-1]  # 定义一个当前指针，指向栈顶节点
                # 上一个打印元素的节点不是当前节点的子节点(说明当前节点子节点需要遍历)，且当前节点的左子节点不为空。
                if tracing != current.left and tracing != current.right and current.left:
                    stack.append(current.left)  # 将当前节点的左子节点压入栈中
                # 如果上一个分支不满足(根据二叉树特点)可知:上一个打印元素的节点是当前节点的子节点，或者当前节点的左子节点为空
                # 上一个打印元素的节点不是当前节点的右子节点，且当前节点的右子节点不为空
                elif tracing != current.right and current.right:
                    stack.append(current.right)  # 将当前节点的右子节点压入栈中
                # 如果以上分支均不满足(根据二叉树特点)可知:上一个打印元素为当前节点的右子节点，或者当前节点无子节点
                else:
                    print(stack.pop().val, end=' ')  # 打印当前节点的元素值
                    tracing = current  # 跟踪指针来到当前指针指向节点
        print('\n')


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

    my_bt = UnrecursiveBinaryTree(n1)
    my_bt.pre_traversal(my_bt.head)
    my_bt.in_traversal(my_bt.head)
    my_bt.pos_traversal(my_bt.head)
    my_bt.advanced_pos_traversal(my_bt.head)
