[927 三等分 cn-leetcode](https://leetcode.cn/problems/three-equal-parts/description/)
<br>给定一个由<kbd>0</kbd>和<kbd>1</kbd>组成的数组<kbd>arr</kbd>，将数组分成**3 个非空的部分**，使得所有这些部分表示相同的二进制值。
<br>如果可以做到，请返回**任何**<kbd>[i, j]</kbd>，其中<kbd>i+1 < j</kbd>，这样一来：
<ul>
<li><kbd>arr[0], arr[1], ..., arr[i]</kbd>为第一部分；</li>
<li><kbd>arr[i + 1], arr[i + 2], ..., arr[j - 1]</kbd>为第二部分；</li>
<li><kbd>arr[j], arr[j + 1], ..., arr[arr.length - 1]</kbd>为第三部分</li>
<li>这三个部分所表示的二进制值相等。</li>
</ul>
如果无法做到，就返回<kbd>[-1, -1]</kbd>。
<br>注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，<kbd>[1,1,0]</kbd>表示十进制中的<kbd>6</kbd>，而不会是<kbd>3</kbd>。此外，前导零也是被允许的，所以<kbd>[0,1,1]</kbd>和<kbd>[1,1]</kbd>表示相同的值。

**示例1**
>输入：
> <br>&emsp;&emsp;arr = [1,0,1,0,1]
> 
>输出：
> <br>&emsp;&emsp;[0,3]

**示例2**
>输入：
> <br>&emsp;&emsp;arr = [1,1,0,1,1]
> 
>输出：
> <br>&emsp;&emsp;[-1,-1]

**示例3**
>输入：
> <br>&emsp;&emsp;arr = [1,1,0,0,1]
> 
>输出：
> <br>&emsp;&emsp;[0,2]

**提示**
<ul>
<li><kbd>3 <= arr.length <= 3 * 10^4</kbd></li>
<li><kbd>arr[i]</kbd> 是<kbd>0</kbd>或<kbd>1</kbd></li>
</ul>

**核心代码模式**

```python
from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        if len(arr) <= 2:  # 如果整体长度<3,那么不能平均分成3份
            return [-1, -1]
        else:
            one_idx = list()  # 存储arr[i] == 1的index
            cnt = 0  # arr[i] == 1的个数，即数组one_idx长度
            # 遍历arr数组，记录arr[i] == 1的位置和总数
            for i in range(len(arr)):
                if arr[i] & 1:
                    one_idx.append(i)
                    cnt += 1
            # →如果arr中没有1，全是0，则返回万能切分[0,2]
            if cnt == 0:
                return [0, 2]
            # →如果1的个数不为3的倍数，或者顺序第2/3 cnt个1的位置上在arr的位置< 2/3 len(arr)，这两种情况均无法切分数组。
            elif cnt % 3 or one_idx[2 * cnt // 3] < 2 / 3 * len(arr):
                return [-1, -1]
            # →剩下就是可以尝试切分的情况
            else:
                f = one_idx[0]
                s = one_idx[cnt // 3]
                t = one_idx[2 * cnt // 3]
                while t < len(arr):
                    if arr[f] == arr[s] and arr[s] == arr[t]:
                        f += 1
                        s += 1
                        t += 1
                    else:  # 如果发现不同，则无法做到切分
                        return [-1, -1]
                return [f - 1, s]
```