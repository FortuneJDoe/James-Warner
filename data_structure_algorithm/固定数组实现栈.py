class Mystack:
    """
    固定数组实现栈
    """

    def __init__(self, size_limit=1):
        """
        初始化栈
        :param size_limit: 栈大小，Default=1
        """

        self.size_limit = size_limit
        self.mystack = [None for _ in range(self.size_limit)]
        self.index = 0

    def push_elem(self, element):
        """
        元素压入栈
        :param element: 压入栈顶元素
        """

        if self.index == self.size_limit:
            print("栈已满，操作无法完成！")
        else:
            self.mystack[self.index] = element
            self.index += 1
            print(f'栈容量{self.size_limit},已用{self.index}。')

    def pop_elem(self):
        """
        元素出栈
        :return: 弹出元素
        """

        if self.index == 0:
            print('空栈无法完成操作！')
        else:
            self.index -= 1
            pop_elem = self.mystack[self.index]
            return pop_elem

    def length(self):
        """
        查询栈内元素个数
        :return: 栈内元素个数
        """

        return self.index
