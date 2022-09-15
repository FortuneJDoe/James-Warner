class Node(object):
    """定义节点类"""

    def __init__(self, element, double=False):
        """
        节点类属性
        :param element: 元素
        :param double: if True 多定义一个前向的last指针，if False 不定义前向last指针，Default: False
        """

        self.element = element
        self.next = None
        if double:
            self.last = None


class MyQueue(object):
    """队列"""

    def __init__(self, node=None):

        self.__head = node

    def is_empty(self):
        
        return self.__head is None

    def length(self):
        cur = self.__head
        le = 0
        while cur:
            le += 1
            cur = cur.next
        return le

    def add(self, item):
        """元素从队列头添加至队列"""

        node = Node(item)
        node.next = self.__head
        self.__head = node

    def pop(self):
        """
        队尾元素出队列
        :return: 返回出队列的元素值
        """

        cur = self.__head
        while cur.next.next:
            cur = cur.next
        pick = cur.next.element
        cur.next = None
        return pick

    def travel(self):
        """遍历整张链表"""

        current = self.__head
        while current:
            print(current.element, end=' ')
            current = current.next
        print("")


class DoubleSideQueue(object):
    """双端队列"""

    def __init__(self, node=None):

        self.__head = node
        self.__tail = node

    def is_empty(self):

        return self.__head is None

    def length(self):

        cur = self.__head
        count = 0
        while cur.next:
            count += 1
            cur = cur.next
        return count

    def add(self, item, side='left'):
        """
        从一端加入队列
        :param item: 入队的元素
        :param side: if left则在左(head)侧外加入元素，if right则从右(tail)侧外加入元素。Default：left
        """

        assert side in ['left', 'right']
        s_dict = {'left': 1, 'right': 0}
        node = Node(item, double=True)

        if self.__head:
            if s_dict[side]:
                cur = self.__head
                self.__head = node
                node.next = cur
                cur.last = node
            elif s_dict[side] == 0:
                cur = self.__tail
                self.__tail = node
                node.last = cur
                cur.next = node
        else:
            self.__head = node
            self.__tail = node

    def pop(self, side='left'):
        """
        从一端出队列
        :param side: if left则删除左(head)端首个元素，if right则删除右(tail)侧首个元素。Default：left
        """

        assert side in ['left', 'right']
        s_dict = {'left': 1, 'right': 0}
        if self.is_empty():
            return False
        else:
            cur = self.__head if s_dict[side] else self.__tail
            if s_dict[side]:
                downstream = cur.next
                self.__head = downstream
                downstream.last = None
            else:
                upstream = cur.last
                self.__tail = upstream
                upstream.next = None
            return cur.element


class MyStack(object):
    """栈"""

    def __init__(self, node=None):

        self.__head = node

    def is_empty(self):

        return self.__head is None

    def length(self):

        cur = self.__head
        count = 0
        while cur.next:
            count += 1
            cur = cur.next
        return count

    def push(self, item):
        """压栈操作"""

        node = Node(item)
        node.next = None if self.__head else self.__head
        self.__head = node

    def pop(self):
        """弹栈操作"""

        if self.__head:
            cur = self.__head
            self.__head = cur.next
            return cur
        else:
            return False


# if __name__ == '__main__':
#     a = Node(0)
#     b = Node(1)
#     c = Node(2)
#     test_01 = MyQueue(a)
#     a.next = b
#     b.next = c
#     empty_01 = test_01.is_empty()
#     l_01 = test_01.length()
#     test_01.travel()
#     test_01.add(3)
#     test_01.travel()
#     p = test_01.pop()
#     test_01.travel()
