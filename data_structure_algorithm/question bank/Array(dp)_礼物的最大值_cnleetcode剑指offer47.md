[剑指Offer 47 礼物的最大价值 cn-leetcode](https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/)
<br>在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值(价值大于 0)
<br>你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角
<br>给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

**示例1**
>输入：
> <br>&emsp;&emsp;[
> <br>&emsp;&emsp;&emsp;[1,3,1],
> <br>&emsp;&emsp;&emsp;[1,5,1],
> <br>&emsp;&emsp;&emsp;[4,2,1]
> <br>&emsp;&emsp;]
> 
>输出：
> <br>&emsp;&emsp;12
> 
>解释：
> <br>&emsp;&emsp;路径 1→3→5→2→1 可以拿到最多价值的礼物

**提示**
<ul>
<li><kbd>0 < grid.length <= 200</kbd></li>
<li><kbd>0 < grid[0].length <= 200</kbd></li>
</ul>

**核心代码模式**

```python
from typing import List

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 当前位置 = [上方位置输出, 左方元素输出, 当前元素值, 当前元素输出]
                grid[i][j] = [0, 0, grid[i][j], 0]
                if i:  # 不是第一行
                    # 当前位置的上方位置输出 = 上方位置的当前元素输出
                    grid[i][j][0] = grid[i - 1][j][3]
                if j:  # 不是第一列
                    # 当前位置的左方位置输出 = 左方位置的当前元素输出
                    grid[i][j][1] = grid[i][j - 1][3]
                # 当前元素输出 = 当前元素分别与上、左输出和的最大值
                # 循环最开始的时候上面两个if都不运行，这恰好就是(0,0)位置输出
                grid[i][j][3] = max(grid[i][j][2] + grid[i][j][0], grid[i][j][2] + grid[i][j][1])
        return grid[-1][-1][-1]
```

**官方题解**

```python
from typing import List

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for j in range(1, n): # 初始化第一行
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m): # 初始化第一列
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
```

<br>&emsp;&emsp;作者：jyd
<br>&emsp;&emsp;链接：https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/solution/mian-shi-ti-47-li-wu-de-zui-da-jie-zhi-dong-tai-gu/
<br>&emsp;&emsp;来源：力扣（LeetCode）
<br>&emsp;&emsp;著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
