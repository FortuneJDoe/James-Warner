[817 链表组件 cn-leetcode](https://leetcode.cn/problems/linked-list-components/)
<br>给定链表头结点<kbd>head</kbd>，该链表上的每个结点都有一个**唯一的整型值**。同时给定列表<kbd>nums</kbd>，该列表是上述链表中整型值的一个子集。
<br>返回列表<kbd>nums</kbd>中组件的个数。
<br>这里对组件的定义为：链表中一段最长连续结点的值(该值必须在列表<kbd>nums</kbd>中)构成的集合。

**示例1**
>输入：
> <br>&emsp;&emsp;head = [0,1,2,3], nums = [0,1,3]
> 
>输出：
> <br>&emsp;&emsp;2
> 
>解释：
> <br>&emsp;&emsp;链表中,0 和 1 是相连接的，且 nums 中不包含 2，所以 [0, 1] 是 nums 的一个组件，同理 [3] 也是一个组件，故返回 2

**示例2**
>输入：
> <br>&emsp;&emsp;head = [0,1,2,3,4], nums = [0,3,1,4]
> 
>输出：
> <br>&emsp;&emsp;2
> 
>解释：
> <br>&emsp;&emsp;链表中，0 和 1 是相连接的，3 和 4 是相连接的，所以 [0, 1] 和 [3, 4] 是两个组件，故返回 2


**核心代码模式**

```python
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0  # 结果：组件个数
        flag = 0  # 状态标记，当前是否在统计中。1：是，0：否
        while head:
            if head.val in nums_set:  # 如果节点值在数组集合中
                flag = 1  # 状态标记变更为 1
            else:  # 如果节点值不在数组集合中
                if flag:  # 如果状态标记为 1
                    ans += 1  # 结果 + 1
                    flag = 0  # 一轮统计结束
            head = head.next  # 指针来到下一个节点
        if flag:  # 跳出循环后，如果状态标记为 1
            ans += 1  #结果 + 1
        return ans
```