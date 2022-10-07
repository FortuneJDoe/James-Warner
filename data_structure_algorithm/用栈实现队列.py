class StacksToQueue:
    """
    用两个栈实现队列
    """

    def __init__(self):
        """
        初始化属性
        """

        self.stack_push = []
        self.stack_pop = []

    def pushtopop(self):
        """
        push栈向pop栈传递数据(在队列的删和查操作前必须完成传递操作)
        """

        if len(self.stack_pop) == 0:  # 必须pop栈为空，才能向pop栈传递数据
            while len(self.stack_push):  # 必须一次性将push栈元素全部传递给pop栈
                self.stack_pop.append(self.stack_push.pop())

    def add_elem(self, element):
        """
        向队列尾部加入元素
        :param element: 压入的元素
        """

        self.stack_push.append(element)

    def pop(self):
        """
        队列头部弹出元素
        :return: 弹出的元素
        """

        if not (self.stack_push and self.stack_pop):  # 两个栈都为空，那么队列为空
            print('Queue is empty, pop operation failed !')
        else:
            self.pushtopop()
            return self.stack_pop.pop()

    def peek(self):
        """
        查询队列头部元素
        :return: 返回队列头步元素
        """

        if not (self.stack_push and self.stack_pop):  # 两个栈都为空，那么队列为空
            print('Queue is empty, peek operation failed !')
        else:
            self.pushtopop()
            return self.stack_pop[-1]
