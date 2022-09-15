class Node(object):
    """定义节点类"""

    def __init__(self, element):
        self.element = element
        self.next = None


class SingleLinkList(object):
    """定义单链表"""

    def __init__(self, node=None):
        """初始化属性定义"""

        self.__head = node

    def is_empty(self):
        """
        判断链表是否为空
        :return:为空时返回True,否则为False
        """

        return self.__head is None

    def length(self):
        """返回链表长度"""

        current = self.__head
        leth = 0
        while current:
            leth += 1
            current = current.next
        return leth

    def travel(self):
        """遍历整张链表"""

        current = self.__head
        while current:
            print(current.element, end=' ')
            current = current.next
        print("")

    def add(self, item):
        """于链表头部添加元素"""

        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """于链表尾部添加元素"""

        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            final = self.__head
            while final.next:
                final = final.next
            final.next = node

    def insert(self, position, item):
        """
        于链表指定索引位置插入元素
        :param item: 被插入元素
        :param position:从0开始
        """

        if position <= 0:
            self.add(item)
        elif position > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            pos = 0
            pre = self.__head
            while pos < position - 1:  # 这样跳出循环时，pre来到position - 1位置，这样元素才可插入到position位置
                pre = pre.next
                pos += 1
            node.next = pre.next
            pre.next = node  # pre【position - 1位置】的next是node【position位置】

    def remove(self, item):
        """
        删除节点
        :param item:需删除的该元素的节点
        # TODO: 将来有机会改成能够删掉全部相同元素的，现在只删遇到的第一个
        """

        current = self.__head

        if current.element == item:
            self.__head = current.next

        else:
            while current.next:
                pre = current
                current = current.next
                if current.element == item:
                    pre.next = current.next
                    break
                else:
                    pass

    def search(self, item):
        """查询链表中是否有与输入相同的元素，有则返回第一个节点索引，无则返回False"""

        current = self.__head

        while current:
            if current.element == item:
                return current
            else:
                current = current.next
        return False

    def reverse(self):
        """反转链表"""

        pre = None
        current = self.__head
        coming = current.next
        while coming:
            current.next = pre
            pre = current
            current = coming
            coming = current.next
        current.next = pre
        self.__head = current


# if __name__ == '__main__':
#     test_l = SingleLinkList()
#     # test_l.append(0)
#     test_l.append(1)
#     test_l.append(2)
#     test_l.append(3)
#     test_l.append(4)
#     test_l.append(5)
#     test_l.add(0)
#     test_l.reverse()
#     test_l.travel()

