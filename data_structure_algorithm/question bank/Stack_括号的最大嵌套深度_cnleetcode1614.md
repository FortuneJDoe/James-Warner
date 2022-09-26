[1614 括号的最大嵌套深度 cn-leetcode](https://leetcode.cn/problems/maximum-nesting-depth-of-the-parentheses/)

[1614 Maximum Nesting Depth of the Parentheses leetcode](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/)

如果字符串满足以下条件之一，则可以称之为**有效括号字符串**(**valid parentheses string**，可以简写为**VPS**):
<ul>
<li>字符串是一个空字符串<kbd>""</kbd>，或者是一个不为<kbd>"("</kbd>或<kbd>")"</kbd>的单字符</li>
<li>字符串可以写为<kbd>AB</kbd>(<kbd>A</kbd>与<kbd>B</kbd>字符串连接)，其中A和B都是**有效括号字符串**</li>
<li>字符串可以写为<kbd>(A)</kbd>，其中<kbd>A</kbd>有效括号字符串 </li>
</ul>

类似地，可以定义任何有效括号字符串<kbd>S</kbd>的 嵌套深度<kbd>depth(S)</kbd>:
<ul>
<li><kbd>depth("") = 0</kbd></li>
<li><kbd>depth(C) = 0</kbd>，其中<kbd>C</kbd>是单个字符的字符串，且该字符不是<kbd>"("</kbd>或<kbd>")"</kbd></li>
<li><kbd>depth(A + B) = max(depth(A), depth(B))</kbd>，其中<kbd>A</kbd>和<kbd>B</kbd>都是**有效括号字符串**</li>
<li><kbd>depth("(" + A + ")") = 1 + depth(A)</kbd>，其中<kbd>A</kbd>是一个**有效括号字符串**</li>
</ul>

例如：<kbd>""、"()()"、"()(()())"</kbd> 都是**有效括号字符串**（嵌套深度分别为 0、1、2），而<kbd>")(" 、"(()"</kbd>都不是**有效括号字符串**。

**输入描述**
<br>给你一个**有效括号字符串**<kbd>s</kbd>

**输出描述**
<br>返回该字符串的<kbd>s</kbd>嵌套深度

**示例1**
>输入：
> <br>&emsp;&emsp;s = "(1+(2*3)+((8)/4))+1"
> 
>输出：
> <br>&emsp;&emsp;3
> 
>解释：
> <br>&emsp;&emsp;数字 8 在嵌套的 3 层括号中

**示例2**
>输入：
> <br>&emsp;&emsp;s = "(1)+((2))+(((3)))"
> 
>输出：
> <br>&emsp;&emsp;3

**核心代码模式**

```python
class Solution:
    def maxDepth(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1 and s != '(' and s != ")":
            return 0
        stack = list()  # 空栈
        count_left = 0  # 累计左括号个数
        m = 0  # 最大左括号个数
        for i in s:
            if i =='(':
                count_left += 1
                m = max(m, count_left)
            elif i == ')':
                count_left -= 1
        return m
```
