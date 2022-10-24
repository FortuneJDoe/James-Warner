[剑指Offer 46 把数字翻译成字符串 cn-leetcode](https://leetcode.cn/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)
<br>给定一个数字，我们按照如下规则把它翻译为字符串：
<br>0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”
<br>请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法

**示例1**
>输入：
> <br>&emsp;&emsp;12258
> 
>输出：
> <br>&emsp;&emsp;5
> 
>解释：
> <br>&emsp;&emsp;12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

**提示**
<ul>
<li><kbd>0 <= num < 2^31</kbd></li>
</ul>

**核心代码模式**

```python
from typing import List

class Solution:
    def fib(self, x: int) -> List[int]:
        """与青蛙跳台阶一样是个斐波那契数列"""
        
        if x == 1:
            return [1]
        elif x == 2:
            return [1, 2]
        else:
            res_list = [1, 2]
            while x - 2:
                res_list.append(res_list[-1] + res_list[-2])
                x -= 1
            return res_list
    
    def translateNum(self, num: int) -> int:
        """
        假设青蛙这次是在爬楼，那么青蛙跳完楼层间台阶时就会中断，走到下个楼梯底部继续跳台阶
        那么这个奇怪的楼有这个特点：
            ① 每个台阶都有一个数字：0~9
            ② 楼层间台阶的数字结尾两级台阶组成数字范围00~09,26~99
        楼层间的台阶数存储在sequence列表中，在楼层间青蛙跳台阶方法或跳1级或跳2级
        :param num: 不区分楼层的台阶序列
        :return: 青蛙爬完楼共有多少种跳台阶的方案组合
        """
        
        if num <= 9:  # 如果只有一级台阶
            return 1
        else:  # 不只一级台阶
            num = str(num)  # 转成字符串，以做切片
            sequence = []  # 楼层间台阶数
            length = 1  # 楼层间台阶计数，起始为1
            m = 1  # 整栋楼最大的楼层间台阶数，最小值为1
            for i in range(1, len(num)):
                if 9 < int(num[i - 1: i + 1]) < 26:  # 当前台阶与上一级台阶组成数字在[10, 25]范围就代表该层没到结尾
                    length += 1  # 该楼层间台阶数+1
                else:  # 结尾了
                    sequence.append(length)  # 把该楼层的台阶数加到集合里
                    m = max(m, length)  # 更新最大台阶数
                    length = 1  # 重置楼层间台阶计数
            sequence.append(length)  # 到天台了，计算一下顶楼到天台的台阶数
            m = max(m, length)
            res = self.fib(m)  # 计算一下不同台阶数的跳法序列
            ans = 1  # 最少有1种跳法
            print(f'sequence:{sequence}')
            print(f'res:{res}')
            for n in sequence:
                ans *= res[n - 1]  # 不同层跳法作积
            return ans
```
