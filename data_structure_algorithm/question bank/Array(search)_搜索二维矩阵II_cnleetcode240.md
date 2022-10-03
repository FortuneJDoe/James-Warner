[240 搜索二维矩阵 cn-leetcode](https://leetcode.cn/problems/search-a-2d-matrix-ii/)
<br>[剑指Offer 04 二维数组中的查找 cn-leetcode](https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/submissions/)
<br>编写一个高效的算法来搜索<kbd>m x n</kbd>矩阵<kbd>matrix</kbd>中的一个目标值<kbd>target</kbd>

<br>该矩阵具有以下特性：
<ul>
<li>每行的元素从左到右升序排列</li>
<li>每列的元素从上到下升序排列</li>
</ul>

**示例1**
![img.png](img.png)
>输入：
> <br>&emsp;&emsp;matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],target = 5
> 
>输出：
> <br>&emsp;&emsp;true

**示例2**
![img_1.png](img_1.png)
>输入：
> <br>&emsp;&emsp;matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],target=20
> 
>输出：
> <br>&emsp;&emsp;false

**提示**
<ul>
<li><kbd>m == matrix.length</kbd></li>
<li><kbd>n == matrix[i].length</kbd></li>
<li><kbd>1 <= n, m <= 300</kbd></li>
<li><kbd>-10^9 <= matrix[i][j] <= 10^9</kbd></li>
<li>每行的所有元素从左到右升序排列</li>
<li>每列的所有元素从上到下升序排列</li>
<li><kbd>-10^9 <= target <= 10^9</kbd></li>
</ul>


**核心代码模式**

```python
from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        else:
            m, n = len(matrix), len(matrix[0])
            x, y = 0, n - 1
            while x < m and y >= 0:
                ans = matrix[x][y]
                if ans == target:
                    return True
                if ans > target:
                    y -= 1
                else:
                    x += 1
            return False
```

### 算法思路

#### 方法三：Z 字形查找

我们可以从矩阵 matrix 的右上角(0,n-1)进行搜索。在每一步的搜索过程中，如果我们位于位置(x,y)，那么我们希望在以 matrix 的左下角为左下角、以(x,y)为右上角的矩阵中进行搜索，即行的范围为[x,m−1]，列的范围为[0,y]：

如果 matrix[x, y] = target，说明搜索完成；

如果 matrix[x, y] > target，由于每一列的元素都是升序排列的，那么在当前的搜索矩阵中，所有位于第 y 列的元素都是严格大于 target 的，因此我们可以将它们全部忽略，即将 y 减少 1；

如果 matrix[x, y] < target，由于每一行的元素都是升序排列的，那么在当前的搜索矩阵中，所有位于第 x 行的元素都是严格小于 target 的，因此我们可以将它们全部忽略，即将 x 增加 1。

在搜索的过程中，如果我们超出了矩阵的边界，那么说明矩阵中不存在 target。

**复杂度分析**
<ul>
<li>时间复杂度: O(m+n)。在搜索的过程中，如果我们没有找到 target，那么我们要么将 y 减少 1，要么将 x 增加 1。由于 (x,y) 的初始值分别为 (0,n−1)，因此 y 最多能被减少 n 次，x 最多能被增加 m 次，总搜索次数为 m+n。在这之后，x 和 y 就会超出矩阵的边界</li>
<li>空间复杂度: O(1)</li>
</ul>

![img_2.png](img_2.png)

![img_3.png](img_3.png)

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/search-a-2d-matrix-ii/solution/sou-suo-er-wei-ju-zhen-ii-by-leetcode-so-9hcx/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。