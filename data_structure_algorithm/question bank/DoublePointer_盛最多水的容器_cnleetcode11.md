[11. 盛最多水的容器 cn-leetcode](https://leetcode.cn/problems/container-with-most-water/)

<br>&emsp;&emsp;给定一个长度为 n 的整数数组<kbd>height</kbd>。有<kbd>n</kbd>条垂线，第 i 条线的两个端点是<kbd>(i, 0)</kbd>和<kbd>(i, height[i])</kbd>。
<br>&emsp;&emsp;找出其中的两条线，使得它们与<kbd>x</kbd>轴共同构成的容器可以容纳最多的水。
<br>&emsp;&emsp;返回容器可以储存的最大水量。
<br>&emsp;&emsp;说明：你不能倾斜容器。

**示例1**
![img_1.png](img_1.png)
>输入：[1,8,6,2,5,4,8,3,7]
> 
>输出：49 
> 
>解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

**示例2**
>输入：height = [1,1]
> 
>输出：1

<br>来源：力扣（LeetCode）
<br>链接：https://leetcode.cn/problems/container-with-most-water
<br>著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

**核心代码**

&emsp;&emsp;双指针法
```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        l = 0
        r = len(height) - 1
        calculator = lambda x,y: min(height[x], height[y]) * (y - x)
        area = calculator(l, r)
        while l < r:
            if height[l] <= height[r]:
                l += 1
                if height[l] <= height[l - 1]:
                    continue
                else:
                    area = calculator(l, r) if area < calculator(l, r) else area
            else:
                r -= 1
                if height[r] <= height[r + 1]:
                    continue
                else:
                    area = calculator(l, r) if area < calculator(l, r) else area
        return area
```

**官网答案**
```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
```
