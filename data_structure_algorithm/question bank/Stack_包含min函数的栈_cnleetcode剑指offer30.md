[剑指Offer 30 包含min函数的栈 cn-leetcode](https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof/)
<br>定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

**题意演示:**
<br>MinStack minStack = new MinStack();
<br>minStack.push(-2);
<br>minStack.push(0);
<br>minStack.push(-3);
<br>minStack.min();      --> 返回 -3.
<br>minStack.pop();
<br>minStack.top();      --> 返回 0.
<br>minStack.min();      --> 返回 -2.


**示例1**
>输入：
> <br>&emsp;&emsp;["MinStack","push","push","push","min","pop","top","min"]
> <br>&emsp;&emsp;[[],[-2],[0],[-3],[],[],[],[]]
> 
>输出：
> <br>&emsp;&emsp;[null,null,null,null,-3,null,0,-2]

**提示**
<br>各函数的调用总次数不超过 20000 次

**核心代码模式**

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.v_stack = []
        self.mv_stack = []

    def push(self, x: int) -> None:
        self.v_stack.append(x)
        self.mv_stack.append(min(x, self.mv_stack[-1]) if self.mv_stack else x)

    def pop(self) -> None:
        self.v_stack.pop()
        self.mv_stack.pop()

    def top(self) -> int:
        return self.v_stack[-1]

    def min(self) -> int:
        return self.mv_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
```

**官方题解**

![剑指offer leetcode官方题解](C:/Users/JayDW/Desktop/jianzhi_30.gif)

按照上面的思路，我们只需要设计一个数据结构，使得每个元素 a 与其相应的最小值 m 时刻保持一一对应。因此我们可以使用一个辅助栈，与元素栈同步插入与删除，用于存储与每个元素对应的最小值。

当一个元素要入栈时，我们取当前辅助栈的栈顶存储的最小值，与当前元素比较得出最小值，将这个最小值插入辅助栈中；

当一个元素要出栈时，我们把辅助栈的栈顶元素也一并弹出；

在任意一个时刻，栈内元素的最小值就存储在辅助栈的栈顶元素中。


时间复杂度：
<br>对于题目中的所有操作，时间复杂度均为 O(1)O(1)。
<br>因为栈的插入、删除与读取操作都是 O(1)O(1)，我们定义的每个操作最多调用栈操作两次。
<br>空间复杂度：O(n)O(n)，其中 nn 为总操作数。最坏情况下，我们会连续插入 nn 个元素，此时两个栈占用的空间为 O(n)O(n)。

题解作者：LeetCode-Solution

来源：力扣（LeetCode）

链接：https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof

著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
