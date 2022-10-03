[leetcode 138 复制带随机指针的链表 cn-leetcode](https://leetcode.cn/problems/copy-list-with-random-pointer/)
<br>[剑指offer 35 复杂链表的复制 cn-leetcode](https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/)

<br>给你一个长度为<kbd>n</kbd>的链表，每个节点包含一个额外增加的随机指针<kbd>random</kbd>，该指针可以指向链表中的任何节点或空节点。
<br>构造这个链表的[深拷贝](https://baike.baidu.com/item/%E6%B7%B1%E6%8B%B7%E8%B4%9D/22785317?fr=aladdin)。深拷贝应该正好由<kbd>n</kbd>个**全新**节点组成，其中每个新节点的值都设为其对应的原节点的值。
<br>新节点的<kbd>next</kbd>指针和<kbd>random</kbd>指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有<kbd>X</kbd>和<kbd>Y</kbd>两个节点，其中<kbd>X.random --> Y</kbd>。那么在复制链表中对应的两个节点<kbd>x</kbd>和<kbd>y</kbd>，同样有<kbd>x.random --> y</kbd>。
<br>返回复制链表的头节点。

用一个由<kbd>n</kbd>个节点组成的链表来表示输入/输出中的链表。每个节点用一个<kbd>[val, random_index]</kbd>表示：
<ul>
<li><kbd>val</kbd>：一个表示<kbd>Node.val</kbd>的整数</li>
<li><kbd>random_index</kbd>：随机指针指向的节点索引（范围从<kbd>0</kbd>到<kbd>n-1</kbd>）；如果不指向任何节点，则为<kbd>null</kbd></li>
</ul>

你的代码**只**接受原链表的头节点<kbd>head</kbd>作为传入参数。

**示例1**
![image](https://user-images.githubusercontent.com/92873873/193556506-280884b5-417b-4556-bd37-fae322ca3fe0.png)

>输入：
> <br>&emsp;&emsp;head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
> 
>输出：
> <br>&emsp;&emsp;[[7,null],[13,0],[11,4],[10,2],[1,0]]

**示例2**
![image](https://user-images.githubusercontent.com/92873873/193556532-2c9cc957-16f7-4671-bdae-b7b832930bfd.png)

>输入：
> <br>&emsp;&emsp;head = [[1,1],[2,1]]
> 
>输出：
> <br>&emsp;&emsp;[[1,1],[2,1]]

**示例3**
![image](https://user-images.githubusercontent.com/92873873/193556558-93585e80-70cd-4891-8d39-ce407350a0f3.png)

>输入：
> <br>&emsp;&emsp;head = [[3,null],[3,0],[3,null]]
> 
>输出：
> <br>&emsp;&emsp;[[3,null],[3,0],[3,null]]

**提示**
<ul>
<li><kbd>0 <= n <= 1000</kbd></li>
<li><kbd>-10^4 <= Node.val <= 10^4</kbd></li>
<li><kbd>Node.random</kbd>为<kbd>null</kbd>或指向链表中的节点</li>
</ul>

**核心代码模式**

```python
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, nex: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = nex
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        cur = head
        h = dict()
        while cur:
            h[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            h[cur].next = h[cur.next] if cur.next else None
            h[cur].random = h[cur.random] if cur.random else None
            cur = cur.next
        return h[head] if head else head
```
