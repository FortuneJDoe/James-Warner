[799 香槟塔 cn-leetcode](https://leetcode.cn/problems/champagne-tower/)
<br>&emsp;&emsp;我们把玻璃杯摆成金字塔的形状，其中**第一层**有<kbd>1</kbd>个玻璃杯，**第二层**有<kbd>2</kbd>个，依次类推到第 100 层，每个玻璃杯(250ml)将盛有香槟
<br>&emsp;&emsp;从顶层的第一个玻璃杯开始倾倒一些香槟，当顶层的杯子满了，任何溢出的香槟都会立刻等流量的流向左右两侧的玻璃杯。
<br>&emsp;&emsp;当左右两边的杯子也满了，就会等流量的流向它们左右两边的杯子，依次类推。
<br>&emsp;&emsp;(当最底层的玻璃杯满了，香槟会流到地板上)

&emsp;&emsp;例如，在倾倒一杯香槟后，最顶层的玻璃杯满了。倾倒了两杯香槟后，第二层的两个玻璃杯各自盛放一半的香槟。在倒三杯香槟后，第二层的香槟满了
<br>&emsp;&emsp;- 此时总共有三个满的玻璃杯。在倒第四杯后，第三层中间的玻璃杯盛放了一半的香槟，他两边的玻璃杯各自盛放了四分之一的香槟，如下图所示

求:现在当倾倒了非负整数杯香槟后，返回第<kbd>i</kbd>行<kbd>j</kbd>个玻璃杯所盛放的香槟占玻璃杯容积的比例(<kbd>i</kbd>和<kbd>j</kbd>都从**0**开始)

**示例1**
>输入：
> <br>&emsp;&emsp;poured(倾倒香槟总杯数) = 1, query_glass(杯子的位置数) = 1, query_row(行数) = 1
> 
>输出：
> <br>&emsp;&emsp;0.00000
> 
>解释：
> <br>&emsp;&emsp;我们在顶层（下标是（0，0））倒了一杯香槟后，没有溢出，因此所有在顶层以下的玻璃杯都是空的

**示例2**
>输入：
> <br>&emsp;&emsp;poured(倾倒香槟总杯数) = 2, query_glass(杯子的位置数) = 1, query_row(行数) = 1
> 
>输出：
> <br>&emsp;&emsp;0.50000
> 
>解释：
> <br>&emsp;&emsp;我们在顶层（下标是（0，0）倒了两杯香槟后，有一杯量的香槟将从顶层溢出，位于（1，0）的玻璃杯和（1，1）的玻璃杯平分了这一杯香槟，所以每个玻璃杯有一半的香槟

**示例3**
>输入：
> <br>&emsp;&emsp;poured = 100000009, query_row = 33, query_glass = 17
> 
>输出：
> <br>&emsp;&emsp;1.00000

**提示**
<ul>
<li><kbd>0 <= poured <= 10^9</kbd></li>
<li><kbd>0 <= query_glass <= query_row < 100</kbd></li>
</ul>

**核心代码模式**

```python
from typing import List

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # 创建“杨辉三角”(所求香槟塔)
        matrix = [list()] * (query_row + 2)  # 一共query_row + 1层香槟塔，再+1层地板
        for row in range(query_row + 2):  # 当层数(row)从0~query_row + 1变化
            matrix[row] = [0] * (row + 1)  # 每层有row + 1列香槟杯
        # 由上至下模拟香槟塔制造过程
        matrix[0][0] = poured  # 流经第一个杯子[0,0]的香槟总量
        for r in range(query_row + 1):  # r从0~query_row行遍历香槟塔的0 → query_row + 1层
            for c in range(r + 1):  # c从0~r列遍历香槟塔的0 → r + 1列
                if matrix[r][c] > 1:
                    # 如果流经当前杯子香槟总量>1，那么向下方相邻两个杯平分多余香槟
                    matrix[r + 1][c] += (matrix[r][c] - 1) / 2
                    matrix[r + 1][c + 1] += (matrix[r][c] - 1) / 2
                    matrix[r][c] = 1  # 当前杯子最终剩余香槟量为1，这句不可省略(否则return语句不是本题所求)。如果所求为“流经杯子香槟总量”，则此句应去掉。
        return matrix[query_row][query_glass]
```