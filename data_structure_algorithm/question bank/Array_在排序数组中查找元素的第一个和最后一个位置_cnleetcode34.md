[leetcode 34 在排序数组中查找元素的第一个和最后一个位置 cn-leetcode](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)
<br>[剑指Offer 53-I 在排序数组中查找数字 I cn-leetcode](https://leetcode.cn/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/?envType=study-plan&id=lcof)

<br>给你一个按照非递减顺序排列的整数数组<kbd>nums</kbd>，和一个目标值<kbd>target</kbd>。
<br>请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值<kbd>target</kbd>，返回<kbd>[-1, -1]</kbd>。

你必须设计并实现时间复杂度为<kbd>O(log n)</kbd>的算法解决此问题

**示例1**
>输入：
> <br>&emsp;&emsp;nums = [5,7,7,8,8,10], target = 8
> 
>输出：
> <br>&emsp;&emsp;[3,4]

**示例2**
>输入：
> <br>&emsp;&emsp;nums = [5,7,7,8,8,10], target = 6
> 
>输出：
> <br>&emsp;&emsp;[-1,-1]

**示例3**
>输入：
> <br>&emsp;&emsp;nums = [], target = 0
> 
>输出：
> <br>&emsp;&emsp;[-1,-1]

**提示**
<ul>
<li><kbd>0 <= nums.length <= 10^5</kbd></li>
<li><kbd>-10^9 <= nums[i] <= 10^9</kbd></li>
<li><kbd>nums</kbd> 是一个非递减数组</li>
<li><kbd>-10^9 <= target <= 10^9</kbd></li>
</ul>

**核心代码模式**
<br>符合题意写法，左右边界均为O(log n)

```python
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or nums[-1] < target or nums[0] > target:
            return [-1, -1]
        else:
            l = 0
            left = 0
            r = len(nums) - 1
            # 第一个二分，找最靠左的target索引
            while l < r:
                mid = l + ((r - l) >> 1)  # 靠左的中点
                if nums[mid] < target:  # 该中点值 < 目标
                    l = mid + 1 # 左边界来到靠右中点(若不+1，若出现计算得到左中点与l重合，出现死循环)
                else:  # 该中点值 => 目标
                    r = mid  # 右边界来到靠左中点
            if nums[l] == target:  # 判断一下二分得到的左边界值是否是target值
                left = l  # 存储左边界位置
                r = len(nums) - 1  # 重置右边界位置
                while l < r:  # 再次二分
                    mid = l + ((r - l) >> 1)  # 靠左的中点
                    if target < nums[mid + 1]:  # 目标 < 靠右中点值
                        r = mid  # 右边界来到靠左中点值
                    else:  # 目标 >= 靠右中点值
                        l = mid + 1  # 左边界来到靠右中点(原因同上)
                return [left, r]
            else:  # 如果找到左边界值不为target，表明target不在nums中，返回[-1, -1]
                return [-1, -1]
```

<br>不符合题意的写法：左边界O(n)，右边界O(log n)
```python
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return [-1, -1]
        else:
            l = -1  # 初始左边界为-1，兼有判断功能
            left = -1  # 存储最靠左的target索引位，不存在则保持初始值-1
            r = len(nums) - 1  # 初始右边界为数组末尾索引
            for i in range(len(nums)):
                if nums[i] == target:
                    l = i
                    left = i
                    break
            if l == -1:
                return [-1, -1]
            while l < r:
                mid = l + ((r - l) >> 1)  # 靠左的中点
                if target < nums[mid + 1]:
                    r = mid
                else:
                    l = mid + 1
            return [left, r]
```
