[剑指Offer 53-II 0~n-1中缺失的数字 I cn-leetcode](https://leetcode.cn/problems/que-shi-de-shu-zi-lcof/)
<br>一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0~n-1之内
<br>在范围0~n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字

**示例1**
>输入：
> <br>&emsp;&emsp;[0,1,3]
> 
>输出：
> <br>&emsp;&emsp;2

**示例2**
>输入：
> <br>&emsp;&emsp;[0,1,2,3,4,5,6,7,9]
> 
>输出：
> <br>&emsp;&emsp;8

**核心代码模式**

```python
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if nums[0] != 0:  # 如果第一个元素不为0
            return 0  # 则缺失的就是0
        elif nums[-1] != len(nums):  # 如果末尾元素不是n
            return len(nums)  # 则缺失的就是n
        else:  # 缺失元素在中间
            for i in range(len(nums) - 1):  # 遍历数组
                if (nums[i] ^ nums[i + 1]) & 1 == 0:  # 如果相邻两数异或运算后末尾不为1
                    return (nums[i] + nums[i + 1]) >> 1  # 则缺失的数即为此两数和的平均数
```

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/que-shi-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。