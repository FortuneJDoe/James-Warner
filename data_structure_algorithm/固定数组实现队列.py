class MyQueue:
    """
    固定数组实现队列(ring Buffer)
    """

    def __init__(self, size_limit=1):
        """
        初始化队列
        :param size_limit: 队列最大长度，Default=1
        """

        self.size_limit = size_limit
        self.myqueue = [None for _ in range(self.size_limit)]
        self.cur_size = 0
        self.push_index = 0
        self.pull_index = 0

    def next_idx(self, i):
        """
        如果当前的下标是i，请返回下一个位置
        :param i: 当前下标
        :return: 下一个位置
        """

        return i + 1 if i < self.size_limit - 1 else 0

    def push_elem(self, element):
        """
        元素压入栈
        :param element: 压入栈顶元素
        """

        if self.cur_size == self.size_limit:
            print("队列已满，操作无法完成！")
        else:
            self.myqueue[self.push_index] = element  # 元素压入队列
            self.cur_size += 1  # 队列当前长度+1
            self.push_index = self.next_idx(self.push_index)  # 更新push指针到“下一个”位置

    def pop_elem(self):
        """
        元素出队列
        :return: 弹出的元素
        """

        if self.cur_size == 0:
            print('空队列无法完成操作！')
        else:
            self.cur_size -= 1
            pop_elem = self.myqueue[self.pull_index]
            self.pull_index = self.next_idx(self.pull_index)
            return pop_elem

    def length(self):
        """
        查询队列内元素个数
        :return: 队列当前元素个数
        """

        return self.cur_size
