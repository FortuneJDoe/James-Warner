[1822. 数组元素积的符号 cn-leetcode](https://leetcode.cn/problems/sign-of-the-product-of-an-array/)
<br>已知函数<kbd>signFunc(x)</kbd>将会根据<kbd>x</kbd>的正负返回特定值：
<ul>
<li>如果<kbd>x</kbd>是正数，返回<kbd>1</kbd></li>
<li>如果<kbd>x</kbd>是负数，返回<kbd>-1</kbd></li>
<li>如果<kbd>x</kbd>是0，返回<kbd>0</kbd></li>
</ul>
<br>给你一个整数数组<kbd>nums</kbd>。令<kbd>product</kbd>为数组<kbd>nums</kbd>中所有元素值的乘积
<br>返回<kbd>signFunc(product)</kbd>


**示例1**
>输入：
> <br>&emsp;&emsp;nums = [-1,-2,-3,-4,3,2,1]
> 
>输出：
> <br>&emsp;&emsp;1
> 
>解释：
> <br>&emsp;&emsp;数组中所有值的乘积是 144 ，且 signFunc(144) = 1

**示例2**
>输入：
> <br>&emsp;&emsp;nums = [1,5,0,2,-3]
> 
>输出：
> <br>&emsp;&emsp;0
> 
>解释：
> <br>&emsp;&emsp;数组中所有值的乘积是 0 ，且 signFunc(0) = 0

**示例3**
>输入：
> <br>&emsp;&emsp;nums = [-1,1,-1,1,-1]
> 
>输出：
> <br>&emsp;&emsp;-1
> 
>解释：
> <br>&emsp;&emsp;数组中所有值的乘积是 -1 ，且 signFunc(-1) = -1

**提示**
<ul>
<li><kbd>1 <= nums.length <= 1000</kbd></li>
<li><kbd>-100 <= nums[i] <= 100</kbd></li>
</ul>

**核心代码模式**

```python
from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if not nums[0]:  # 若首个元素为0，
            return 0  # 则返回0
        else:
            eor = nums[0]  # 首个元素计入eor(Exclusive OR)
            for i in nums[1:]:  # 遍历数组
                if not i:  # 如果元素为0
                    return 0  #返回0
                else:  # 如果元素不为0
                    eor ^= i  # 进行异或
            if eor >= 0:  # 如果eor结果不为负，则表示数组不含0且有偶数个负数元素
                return 1  # 乘积为正数，返回1
            else:  # 否则，数组不含0且有奇数个负数
                return -1  # 乘积为负数，返回-1
```
