[481 神奇字符串 cn-leetcode](https://leetcode.cn/problems/magical-string/)
<br>神奇字符串<kbd>s</kbd>仅由<kbd>'1'</kbd>和<kbd>'2'</kbd>组成，并需要遵守下面的规则：
<ul>
<li>神奇字符串<kbd>s</kbd>的神奇之处在于，串联字符串中<kbd>'1'</kbd>和<kbd>'2'</kbd>的连续出现次数可以生成该字符串。</li>
</ul>
<kbd>s</kbd>的前几个元素是<kbd>s = "1221121221221121122……"</kbd>
<br>如果将<kbd>s</kbd>中连续的若干<kbd>'1'</kbd>和<kbd>'2'</kbd>进行分组，可以得到<kbd>"1 22 11 2 1 22 1 22 11 2 11 22 ......"</kbd>
<br>每组中<kbd>'1'</kbd>或者<kbd>'2'</kbd>的出现次数分别是<kbd>"1 2 2 1 1 2 1 2 2 1 2 2 ......"</kbd>。上面的出现次数正是<kbd>s</kbd>自身

求：给你一个整数<kbd>n</kbd>，返回在神奇字符串<kbd>s</kbd>的前<kbd>n</kbd>个数字中<kbd>1</kbd>的数目

**示例1**
>输入：
> <br>&emsp;&emsp;n = 6
> 
>输出：
> <br>&emsp;&emsp;3
> 
>解释：
> <br>神奇字符串 s 的前 6 个元素是 “122112”，它包含三个 1，因此返回 3 

**示例1**
>输入：
> <br>&emsp;&emsp;n = 1
> 
>输出：
> <br>&emsp;&emsp;1


**提示**
<ul>
<li><kbd>1 <= n <= 10^5</kbd></li>
</ul>

**核心代码模式**

```python
from typing import List

class Solution:
    def magicalString(self, n: int) -> int:
        s = '122'  # 字符串初始化
        mark = 2  # mark代表s的一个参考位置的索引值，初始为2位置
        cnt = 1  # 记录s中1的个数
        h = {'1':'2','2':'1'}
        # 开始生成后续字符串进行拼接
        # 核心逻辑: s[-1]字符决定生成字符串的内容;mark位置的字符决定生成的字符串长度
        while n - len(s) > 0:
            s += h[s[-1]] * int(s[mark])  # 内容 * 长度
            cnt += int(s[mark]) if s[-1] == '1' else 0  # 如果生成内容为1，则更新cnt
            mark += 1  # mark索引+1
            # print(f'字符串s：{s}')
        cnt -= 1 if (len(s) > n and s[-1] == '1') else 0  # debug:如果最后一次生成‘11’且造成字符串长度 > n, 则1的个数要-1
        return cnt
```
