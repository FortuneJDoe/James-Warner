[剑指Offer 32-II 从上到下打印二叉树 II cn-leetcode](https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/)
<br>从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

**示例1**
>输入：
> <br>&emsp;&emsp;给定二叉树: [3,9,20,null,null,15,7]
> 
>输出：
> <br>&emsp;&emsp;[
  [3],
  [9,20],
  [15,7]
]


**核心代码模式**

```python
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = list()
        if root:
            cur_end = root  # 默认头节点为当前层最后节点
            next_end = None  # 下一层尾结点(最右节点)，初始值默认None
            queue = list()  # 队列，用作中转
            queue.append(root)  # 首先从尾部压入头节点
            temp = list()  # 根据题目要求，准备一个“小队列”存储每层元素
            while queue:  # 当中转队列不为空
                cur = queue.pop(0)  # 头部弹出节点，cur指针来到被弹出节点
                temp.append(cur.val)  # 小队列压入当前节点的元素值
                # 1. 如果下一层有子节点，就继续压入中转队列
                # 2. 下一层尾结点的指针指向被压入中转队列的节点
                if cur.left:
                    queue.append(cur.left)
                    next_end = cur.left
                if cur.right:
                    queue.append(cur.right)
                    next_end = cur.right
                # 如果被弹出节点就是当前层的尾结点(最右节点)
                if cur == cur_end:
                    ans.append(temp)  # answer压入当前层元素队列
                    cur_end = next_end  # 结算，当前层最右节点指针指向下一层最右节点
                    temp = list()  # 结算，小队列重置
        return ans
```