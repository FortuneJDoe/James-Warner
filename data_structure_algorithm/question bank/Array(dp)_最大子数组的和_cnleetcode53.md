[53 最大子数组和 cn-leetcode](https://leetcode.cn/problems/maximum-subarray/)
<br>[剑指Offer 42 连续子数组的最大和 cn-leetcode](https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/)
<br>给你一个整数数组<kbd>nums</kbd>，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和
<br>**子数组**是数组中的一个连续部分

**示例1**
>输入：
> <br>&emsp;&emsp;nums = [-2,1,-3,4,-1,2,1,-5,4]
> 
>输出：
> <br>&emsp;&emsp;6
> 
>解释：
> <br>&emsp;&emsp;连续子数组 [4,-1,2,1] 的和最大，为 6

**示例2**
>输入：
> <br>&emsp;&emsp;nums = [1]
> 
>输出：
> <br>&emsp;&emsp;1

**示例3**
>输入：
> <br>&emsp;&emsp;nums = [5,4,-1,7,8]
> 
>输出：
> <br>&emsp;&emsp;23

**提示**
<ul>
<li><kbd>1 <= nums.length <= 10^5</kbd></li>
<li><kbd>-10^4 <= nums[i] <= 10^4</kbd></li>
</ul>

**核心代码模式**

```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] >= 0:
                nums[i] += nums[i - 1]
        return max(nums)
```

![37e0236f27d9a2579852d4f06403d23](https://user-images.githubusercontent.com/92873873/197192434-e9b6c9a8-2a1b-4d91-afa0-70c09fa3a9a9.png)
[来源：力扣官方题解视频截图](https://leetcode.cn/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/)
