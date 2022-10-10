[剑指Offer 26 树的子结构 cn-leetcode](https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/)
<br>输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
<br>B是A的子结构， 即 A中有出现和B相同的结构和节点值

**示例1**
>输入：
> <br>&emsp;&emsp;A = [1,2,3], B = [3,1]
> 
>输出：
> <br>&emsp;&emsp;false

**示例2**
>输入：
> <br>&emsp;&emsp;A = [3,4,5,1,2], B = [4,1] (按层遍历格式)
> 
>输出：
> <br>&emsp;&emsp;true


**核心代码模式**

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:  # 题意明确：约定空树不是任意一个树的子结构
            return False
        queue = list()
        queue.append(A)
        cur = None
        while queue:
            cur = queue.pop(0)
            if cur.val == B.val:  # 如果被弹出节点的值与B头节点的值相等
                queue_a = list()
                queue_b = list()
                queue_a.append(cur)
                queue_b.append(B)
                flag = 1  # 立一个flag，当下面的while循环被打断跳出的时候更新值为0
                while queue_b:  # B树节点的栈不为空
                    # B树的先序遍历为主导，与A树对应起始节点逐一对比
                    cur_b = queue_b.pop(0)
                    from_A_tree = queue_a.pop(0)
                    if not from_A_tree:  # 如果弹出的A树节点为空(代表B数有节点，但A树已无对应节点)
                        return False
                    elif from_A_tree.val == cur_b.val:  # 对应节点的值相等
                        # 只要B树子节点不为空，无论A树是否有子节点，都压入对应栈中，进入下一循环
                        if cur_b.left:
                            queue_a.append(from_A_tree.left)
                            queue_b.append(cur_b.left)
                        if cur_b.right:
                            queue_a.append(from_A_tree.right)
                            queue_b.append(cur_b.right)
                    # 两树当前节点的值出现不相等
                    else:
                        flag = 0
                        break  # 跳出循环，寻找下一处相等值的节点
                # while循环跳出，需要判断是否为因为节点值不相等而结束
                if len(queue_b) == 0 and flag:
                    return True
            # 如果进行到这一步，证明A树当前节点开始的子树 != B树，需要接续遍历A树
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return False


if __name__ == '__main__':
    A = TreeNode(1)
    n1 = TreeNode(0)
    n2 = TreeNode(1)
    n3 = TreeNode(-4)
    n4 = TreeNode(-3)
    A.left = n1
    A.right = n2
    n1.left = n3
    n1.right = n4
    B = TreeNode(1)
    n5 = TreeNode(-4)
    B.left = n5

    judge = Solution()
    judge.isSubStructure(A, B)
```