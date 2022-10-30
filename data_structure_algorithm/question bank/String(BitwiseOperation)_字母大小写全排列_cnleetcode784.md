[784 字母大小写全排列 cn-leetcode](https://leetcode.cn/problems/letter-case-permutation/)
<br>给定一个字符串<kbd>s</kbd>，通过将字符串<kbd>s</kbd>中的每个字母转变大小写，我们可以获得一个新的字符串
返回*所有可能得到的字符串集合*。以**任意顺序**返回输出

**示例1**
>输入：
> <br>&emsp;&emsp;s = "a1b2"
> 
>输出：
> <br>&emsp;&emsp;["a1b2", "a1B2", "A1b2", "A1B2"]

**示例2**
>输入：
> <br>&emsp;&emsp;s = "3z4"
> 
>输出：
> <br>&emsp;&emsp;["3z4","3Z4"]


**提示**
<ul>
<li><kbd>1 <= s.length <= 12</kbd></li>
<li><kbd>s</kbd>由小写英文字母、大写英文字母和数字组成</li>
</ul>

**核心代码模式**

```python
from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s = s.lower()  # 全变成小写字母
        ans = [s,]  # s为返回值列表中的首个元素
        devide_s = []  # 拆分字符串
        indice = []  # 存储字母位置的索引的列表
        for e in range(len(s)):
            if s[e].islower():
                indice.append(e)
            devide_s.append(s[e])
        num = 1  # 二进制字符串的十进制值，位数与indice一致。
        # 核心逻辑：如果二进制第k位(从0起始)为1，则s[indice[k]]变换为为大写字母
        temp = []  # 缓存单元
        while num < 2 ** len(indice):  # 存在num个字母，则ans中有2 ** num个元素
            for k in range(len(indice)):  # 遍历字母索引列表
                if (num >> k) & 1:  # 如果二进制第k位(从0起始)为1
                    devide_s[indice[k]] = devide_s[indice[k]].upper()  # 则s[indice[k]]变换为为大写字母
                else:  # 否则
                    devide_s[indice[k]] = devide_s[indice[k]].lower()  # 为小写字母
            ans.append(''.join(devide_s))  # 添加结果
            num += 1
        return ans
```
