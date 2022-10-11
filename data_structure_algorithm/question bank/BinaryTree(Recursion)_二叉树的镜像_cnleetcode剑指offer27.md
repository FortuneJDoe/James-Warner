[剑指Offer 27 二叉树的镜像 cn-leetcode](https://leetcode.cn/problems/er-cha-shu-de-jing-xiang-lcof/)
<br>请完成一个函数，输入一个二叉树，该函数输出它的镜像

**示例1**
>输入：
> <br>&emsp;&emsp;root = [4,2,7,1,3,6,9]
> 
>输出：
> <br>&emsp;&emsp;[4,7,2,9,6,3,1]


**核心代码模式**

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        # 1. 先序遍历，序列化
        def pre_s(start: TreeNode, ans: list):
            if start:
                ans.append(start.val)
                pre_s(start.left, ans)
                pre_s(start.right, ans)
            else:
                ans.append(None)
        
        def pre_serial(start: TreeNode):
            ans = list()
            pre_s(start, ans)
            return ans

        a = pre_serial(root)
        
        # 2. 按头→右→左遍历顺序反序列化
        def pre_build(prelist: list):
            value = prelist.pop(0)
            if value:
                head = TreeNode(value)
                head.right = pre_build(prelist)  # 注意先right
                head.left = pre_build(prelist)
                return head
            else:
                return None
        
        def pre_b_by_queue(prelist: list):
            if prelist:
                return pre_build(prelist)
            else:
                return None
        
        return pre_b_by_queue(a)
```


**官方题解**

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        left = self.mirrorTree(root.left)
        right = self.mirrorTree(root.right)
        root.left, root.right = right, left
        return root
```

作者：LeetCode-Solution
<br>链接：https://leetcode.cn/problems/er-cha-shu-de-jing-xiang-lcof/solution/er-cha-shu-de-jing-xiang-by-leetcode-sol-z44i/
<br>来源：力扣（LeetCode）
<br>著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。