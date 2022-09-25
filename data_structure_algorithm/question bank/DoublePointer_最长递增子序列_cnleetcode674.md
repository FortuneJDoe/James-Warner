[674 最长连续递增序列 cn-leetcode](https://leetcode.cn/problems/longest-continuous-increasing-subsequence/)

给定一个未经排序的整数数组，找到最长且**连续递增的子序列**，并返回该序列的长度。
<br>**连续递增的子序列**可以由两个下标<kbd>l</kbd>和<kbd>r(l < r)</kbd>确定，
<br>如果对于每个<kbd>l <= i < r</kbd>，都有<kbd>nums[i] < nums[i + 1]</kbd>，
<br>那么子序列<kbd>[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]</kbd>就是连续递增子序列。

**示例1**
>输入：
> <br>&emsp;&emsp;nums = [1,3,5,4,7]
> 
>输出：
> <br>&emsp;&emsp;3
> 
>解释：
> <br>&emsp;&emsp;最长连续递增序列是 [1,3,5], 长度为3。
> <br>&emsp;&emsp;尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。

**示例2**
>输入：
> <br>&emsp;&emsp;nums = [2,2,2,2,2]
> 
>输出：
> <br>&emsp;&emsp;1
> 
>解释：
> <br>&emsp;&emsp;最长连续递增序列是 [2], 长度为1。

**提示**
<br><kbd>1 <= nums.length <= 104</kbd>
<br><kbd>-109 <= nums[i] <= 109</kbd>

**核心代码模式**

```python
from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        m = 0
        l = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                m = max(m, i - l)
                l = i
        m = max(m, len(nums) - l)
        return m
```
