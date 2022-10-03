[154 寻找旋转排序数组中的最小值 II cn-leetcode](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/)
<br>[剑指Offer 11 旋转数组的最小数字 cn-leetcode](https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)
<br>(简单版的[153 寻找旋转排序数组中的最小值 cn-leetcode](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/))
<br>已知一个长度为<kbd>n</kbd>的数组，预先按照升序排列，经由<kbd>1</kbd>到<kbd>n</kbd>次**旋转**后，得到输入数组。
<br>例如，原数组<kbd>nums = [0,1,4,4,5,6,7]</kbd>在变化后可能得到：
<ul>
<li>若旋转<kbd>4</kbd>次，则可以得到<kbd>[4,5,6,7,0,1,4]</kbd></li>
<li>若旋转<kbd>7</kbd>次，则可以得到<kbd>[4,5,6,7,0,1,4]</kbd></li>
</ul>

注意，数组<kbd>[a[0], a[1], a[2], ..., a[n-1]]</kbd>旋转一次 的结果为数组<kbd>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</kbd>
<br>给你一个可能存在**重复**元素值的数组<kbd>nums</kbd>，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的**最小元素**

**你必须尽可能减少整个过程的操作步骤**

**示例1**
>输入：
> <br>&emsp;&emsp;nums = [1,3,5]
> 
>输出：
> <br>&emsp;&emsp;1

**示例2**
>输入：
> <br>&emsp;&emsp;nums = [2,2,2,0,1]
> 
>输出：
> <br>&emsp;&emsp;0

**示例3**
>输入：
> <br>&emsp;&emsp;nums = [10,1,10,10,10]
> 
>输出：
> <br>&emsp;&emsp;1

**提示**
<ul>
<li><kbd>n == nums.length</kbd></li>
<li><kbd>1 <= n <= 5000</kbd></li>
<li><kbd>-5000 <= nums[i] <= 5000</kbd></li>
<li><kbd>nums</kbd>原来是一个升序排序的数组，并进行了<kbd>1</kbd>至<kbd>n</kbd>次旋转</li>
</ul>


**核心代码模式**

```python
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return False
        elif nums[0] < nums[-1]:
            return nums[0]
        else:
            l = 0
            r = len(nums) - 1
            while l < r:
                mid = l + ((r - l) >> 1)  # 靠左中点
                if nums[mid] > nums[r]:
                    l = mid + 1
                elif nums[mid] < nums[r]:
                    r = mid
                else:
                    r -= 1
            print(l, r)
            return nums[l]
```

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。