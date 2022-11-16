[775 全局倒置与局部倒置 cn-leetcode](https://leetcode.cn/problems/global-and-local-inversions/description/)
<br>给你一个长度为<kbd>n</kbd>的整数数组<kbd>nums</kbd>，表示由范围<kbd>[0, n - 1]</kbd>内所有整数组成的一个排列。
<br>**全局倒置**的数目等于满足下述条件不同下标对<kbd>(i, j)</kbd>的数目：
<ul>
<li><kbd>0 <= i < j < n</kbd></li>
<li><kbd>nums[i] > nums[j]</kbd></li>
</ul>
<br>**局部倒置**的数目等于满足下述条件不同下标对<kbd>i</kbd>的数目：
<ul>
<li><kbd>0 <= i < n - 1</kbd></li>
<li><kbd>nums[i] > nums[i + 1]</kbd></li>
</ul>
当数组<kbd>nums</kbd>中**全局倒置**的数量等于**局部倒置**的数量时，返回<kbd>true</kbd>；否则，返回<kbd>false</kbd>。

**示例1**
>输入：
> <br>&emsp;&emsp;nums = [1,0,2]
> 
>输出：
> <br>&emsp;&emsp;true
> 
>解释：
> <br>&emsp;&emsp;有 1 个全局倒置，和 1 个局部倒置。

**示例2**
>输入：
> <br>&emsp;&emsp;nums = [1,2,0]
> 
>输出：
> <br>&emsp;&emsp;false
> 
>解释：
> <br>&emsp;&emsp;有 2 个全局倒置，和 1 个局部倒置。

**提示**
<ul>
<li><kbd>n == nums.length</kbd></li>
<li><kbd>1 <= n <= 10^5</kbd></li>
<li><kbd>0 <= nums[i] < n</kbd></li>
<li><kbd>nums</kbd>中的所有整数<strong>互不相同</strong></li>
<li><kbd>nums</kbd>是范围<kbd>[0, n - 1]</kbd>内所有数字组成的一个排列</li>
</ul>

**核心代码模式**

```python
from typing import List

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        """
        1. nums为[0, n-1]的n个互不相等的整数构成
        2. 如果一个倒置是局部倒置，那么它一定也是一个全局倒置
        根据题意，当|nums[i] - i| > 1时，必存在全局倒置数量 > 局部倒置数量
        """

        for i in range(len(nums)):
            if abs(nums[i] - i) > 1:
                return False
        return True
```