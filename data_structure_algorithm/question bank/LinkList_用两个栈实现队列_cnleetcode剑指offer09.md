[剑指offer 09 用两个栈实现队列 cn-leetcode](https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/?plan=lcof&plan_progress=sisubu6)
<br>用两个栈实现一个队列。队列的声明如下，请实现它的两个函数<kbd>appendTail</kbd>和<kbd>deleteHead</kbd>，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，<kbd>deleteHead</kbd>操作返回 -1)

**示例1**
>输入：
> <br>&emsp;&emsp;["CQueue","appendTail","deleteHead","deleteHead","deleteHead"]
> <br>&emsp;&emsp;[[],[3],[],[],[]]
> 
>输出：
> <br>&emsp;&emsp;[null,null,3,-1,-1]

**示例2**
>输入：
> <br>&emsp;&emsp;["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
> <br>&emsp;&emsp;[[],[],[5],[2],[],[]]
> 
>输出：
> <br>&emsp;&emsp;[null,-1,null,null,5,2]

**提示**
<ul>
<li><kbd>1 <= values <= 10000</kbd></li>
<li>最多会对<kbd>appendTail</kbd>和<kbd>deleteHead</kbd>进行<kbd>10000</kbd>次调用</li>
</ul>

**核心代码模式**

```python
class Node:
    """声明一个节点(Node)类"""

    def __init__(self, element=None):
        """
        初始化Node属性
        :param element: 节点元素
        """
        
        self.element = element  # 存储元素值
        self.next = None  # 存储指向下个节点的地址

class CQueue:
    """队列"""

    def __init__(self, node:Node=None):
        """
        初始化队列属性
        :param node: 输入节点(为Node类或者None)
        """
        self.head = node  # 头节点
        self.tail = node  # 尾结点

    def appendTail(self, value: int) -> None:
        """
        在队尾添加节点
        :param value: 加入队列的元素(int类型)
        """
        
        node = Node(value)  # 将元素转换成Node类
        if self.tail:  # 如果尾结点不为空，即队列不为空
            self.tail.next = node  # 尾指针指向新加入的节点
            self.tail = node  # 尾指针来到新的队尾
        else:  # 如果队列为空，则执行__init__()的内容
            self.head = node
            self.tail = node

    def deleteHead(self) -> int:
        """
        队首元素弹出队列
        """
        
        if self.head:  # 如果队列不为空
            pop = self.head  # 找到头节点
            self.head = self.head.next  # 队列第二个节点(或者None)成为新的头结点
            if self.head is None:  # 如果队列空了
                self.tail = self.head  # 尾结点与头结点保持一致
            return pop.element  # 返回弹出节点的元素
        else:  # 如果队列为空
            return -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```

来源：力扣（LeetCode）

链接：https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof

著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
