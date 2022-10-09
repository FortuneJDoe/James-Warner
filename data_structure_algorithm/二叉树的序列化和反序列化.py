class Node(object):
    """二叉树节点"""

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class SerializedAndReconstructTree(object):
    """二叉树按层打印及寻找最大宽度"""

    def __init__(self, node=None):
        self.head = node

    def level_serial(self, start: Node):
        """按层遍历二叉树"""

        ans = list()  # 序列化结果
        # 无论头节点是否为空都要进行序列化，当头节点不为空则压入队列
        if start:
            ans.append(start.val)  # 序列化是加入节点的值
            queue = list()  # 队列存储不为空的节点
            queue.append(start)
            while queue:  # 队列不为空
                start = queue.pop(0)  # 从头部弹出节点
                # 无论子节点是否为空，都进行序列化。当子节点为空时压入队列。
                if start.left:
                    ans.append(start.left.val)
                    queue.append(start.left)
                else:
                    ans.append(None)
                if start.right:
                    ans.append(start.right.val)
                    queue.append(start.right)
                else:
                    ans.append(None)
        else:  # 头节点为空，直接序列化
            ans.append(None)
        return ans  # 返回序列化结果

    def generateNode(self, value):
        """建立节点"""

        if value:
            return Node(value)
        else:
            return None

    def buildByLevelQueue(self, level_list: list):
        """根据按层遍历序列化结果，进行反序列化"""

        if level_list:  # 序列不为空
            head = self.generateNode(level_list.pop(0))  # 建立头节点
            queue = list()  # 准备空队列
            if head:  # 头节点不为空
                queue.append(head)  # 节点压入队列
            while queue:  # 队列不为空
                node = queue.pop(0)  # 弹出头节点，node指针指向被弹出元素
                node.left = self.generateNode(level_list.pop(0))  # 建立左子节点或空
                node.right = self.generateNode(level_list.pop(0))  # 建立右子节点或空
                if node.left:  # 如果左子节点不为空
                    queue.append(node.left)  # 左子节点压入队列尾部
                if node.right:  # 如果右子节点不为空
                    queue.append(node.right)  # 右子节点压入队列尾部
            return head
        else:
            return None

    def pres(self, start: Node, ans: list):
        """先序遍历，将遍历到的元素压入传入的队列ans中"""

        if start:
            ans.append(start.val)
            self.pres(start.left, ans)
            self.pres(start.right, ans)
        else:
            ans.append(None)  # None也要压入队列占位

    def preSerial(self, start: Node):
        """先序遍历序列化"""

        ans = list()
        self.pres(start, ans)
        return ans

    def preb(self, prelist: list):
        """根据先序遍历生辰的序列，进行反序列化"""

        value = prelist.pop(0)
        if value:
            head = Node(value)
            head.left = self.preb(prelist)
            head.right = self.preb(prelist)
            return head
        else:
            return None

    def buildByPreQueue(self, prelist: list):
        """先序遍历的反序列化"""

        if prelist:
            return self.preb(prelist)
        else:
            return None


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n5.left = n8
    n6.right = n9

    my_bt = SerializedAndReconstructTree(n1)
    a = my_bt.preSerial(n1)
    print(a)
    b = my_bt.buildByPreQueue(a)
    c = my_bt.level_serial(n1)
    print(c)
    d = my_bt.buildByLevelQueue(c)
