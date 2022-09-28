[剑指 Offer 06 从尾到头打印链表 cn-leetcode](https://leetcode.cn/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/)
<br>输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）

**示例1**
>输入：
> <br>&emsp;&emsp;head = [1,3,2]
> 
>输出：
> <br>&emsp;&emsp;[2,3,1]

**提示**
<br>0 <= 链表长度 <= 10000

**核心代码模式**

```python
"""--snip--"""
```

**官方题解**

### 1. 递归法

```python
# Definition for singly-linked list.
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        return self.reversePrint(head.next) + [head.val] if head else []
```

**算法流程：**
<ol>
<li>递推阶段： 每次传入 head.next ，以 head == None（即走过链表尾部节点）为递归终止条件，此时返回空列表[] </li>
<li>回溯阶段： 利用 Python 语言特性，递归回溯时每次返回 当前 list + 当前节点值 [head.val] ，即可实现节点的倒序输出</li>
</ol>

**复杂度分析：**
<br>时间复杂度 O(N)O(N)： 遍历链表，递归 NN 次
<br>空间复杂度 O(N)O(N)： 系统递归需要使用 O(N)O(N) 的栈空间。

### 2. 辅助栈法

```python
# Definition for singly-linked list.
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
```


**算法流程：**
<ol>
<li>入栈： 遍历链表，将各节点值 push 入栈。（Python 使用 append() 方法，Java借助 LinkedList 的addLast()方法）</li>
<li>出栈： 将各节点值 pop 出栈，存储于数组并返回。（Python 直接返回 stack 的倒序列表，Java 新建一个数组，通过 popLast() 方法将各元素存入数组，实现倒序输出）</li>
</ol>

**复杂度分析：**
<br>时间复杂度 O(N)O(N)： 入栈和出栈共使用 O(N)O(N) 时间。
<br>空间复杂度 O(N)O(N)： 辅助栈 stack 和数组 res 共使用 O(N)O(N) 的额外空间。

作者：jyd
<br>链接：https://leetcode.cn/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/solution/mian-shi-ti-06-cong-wei-dao-tou-da-yin-lian-biao-d/
<br>来源：力扣（LeetCode）
<br>著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
