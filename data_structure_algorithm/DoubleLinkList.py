class Node(object):
    """定义节点类"""

    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None


class DoubleLinkList(object):
    """双链表"""

    def __init__(self, node=None):
        """初始化属性"""

        self.__head = node
        self.__tail = node

    def is_empty(self):
        """
        判断链表是否为空
        :return:为空时返回True,否则为False
        """

        return self.__head is None

    def length(self):
        """返回链表长度"""

        current_position = self.__head
        leth = 0
        while current_position:
            leth += 1
            current_position = current_position.right
        return leth

    def travel(self, direction='right'):
        """
        遍历整张链表
        :param direction: if right则从左(head)到右(tail)遍历，if left则从右(tail)到左(head)遍历。Default：right
        """

        assert direction in ['right', 'left']
        d = {'right': 1, 'left': 0}
        current_position = self.__head if d[direction] else self.__tail
        while current_position:
            print(current_position.element, end=' ')
            current_position = current_position.right if d[direction] else current_position.left
        print("")

    def add(self, item, side='left'):
        """
        从端点加入元素
        :param item: 被加入的元素
        :param side: if left则在左(head)侧外加入元素，if right则从右(tail)侧外加入元素。Default：left
        """

        assert side in ['right', 'left']
        node = Node(item)
        d = {'right': 0, 'left': 1}
        if d[side]:
            current = self.__head
            self.__head = node
            node.right = current
            current.left = node
        else:
            current = self.__tail
            self.__tail = node
            node.left = current
            current.right = node

    def insert(self, position, item):
        """
        于链表指定索引位置插入元素
        :param item: 被插入元素
        :param position:从左侧0位置开始
        """

        if position <= 0:
            self.add(item, side='left')
        elif position > self.length() - 1:
            self.add(item, side='right')
        else:
            node = Node(item)
            pos = 0
            pre = self.__head
            while pos < position - 1:  # 这样跳出循环时，pre来到position - 1位置，这样元素才可插入到position位置
                pre = pre.right
                pos += 1
            node.right = pre.right
            pre.right.left = node  # pre【position - 1位置】的next是node【position位置】
            pre.right = node
            node.left = pre

    def remove(self, item, direction='right'):
        """
        删除节点
        :param item:需删除的该元素的节点
        :param direction:  if right则从左(head)到右(tail)遍历，if left则从右(tail)到左(head)遍历。Default：right
        # TODO: 将来有机会改成能够删掉全部相同元素的，现在只删遇到的第一个
        """

        assert direction in ['right', 'left']
        d = {'right': 1, 'left': 0}
        if d[direction]:
            current = self.__head
            pre = current.left
            post = current.right
            while post:
                if current != item:
                    pre = current
                    current = post
                    post = post.right
                else:
                    post.left = pre
                    if pre is None:
                        self.__head = post
                    else:
                        pre.right = post
                    break
            if current == item:
                if pre is None:
                    self.__head = None
                    self.__tail = None
                else:
                    pre.right = post
                    self.__tail.left = pre
            else:
                print(f'No {item}')

        # TODO 从右侧开始删的以后再写

    def search(self, item, direction='right'):
        """
        查询链表中是否有与输入相同的元素，有则返回第一个节点索引，无则返回False
        :param item: 需查询的该元素
        :param direction: if right则从左(head)到右(tail)遍历搜索，if left则从右(tail)到左(head)遍历。Default：right
        :return:
        """

        # TODO 待续

    def reverse(self):
        """反转链表"""

        prior = None
        current = self.__head
        self.__tail = current
        while current:
            post = current.right
            current.right = prior
            current.left = post
            prior = current
            current = post
        self.__head = prior

