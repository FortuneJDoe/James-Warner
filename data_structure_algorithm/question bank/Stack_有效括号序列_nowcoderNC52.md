[NC52 有效括号序列 nowcoder](https://www.nowcoder.com/practice/37548e94a270412c8b9fb85643c8ccc2?tpId=196&tqId=37083&rp=1&ru=/exam/oj&qru=/exam/oj&sourceUrl=%2Fexam%2Foj%3Fpage%3D2%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D196&difficulty=undefined&judgeStatus=undefined&tags=&title=)

给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
<br>括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。

数据范围：字符串长度 0≤n≤10000
<br>进阶：时间复杂度：O(n) ，空间复杂度：O(n)

**输入描述**
<br>第一行输入要排序的人的个数n，
<br>第二行输入一个整数表示排序的方式，
<br>之后n行分别输入他们的名字和成绩，以一个空格隔开

**输出描述**
<br>按照指定方式输出名字和成绩，名字和成绩之间以一个空格隔开

**示例1**
>输入：
> <br>&emsp;&emsp;"["
> 
>输出：
> <br>&emsp;&emsp;False

**示例2**
>输入：
> <br>&emsp;&emsp;"[]"
> 
>输出：
> <br>&emsp;&emsp;True

**核心代码模式**

```python
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return bool布尔型
#
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:  # 如果s长度不足，有效括号无从谈起
            return False
        h_press = {"(": ")", "[": "]", "{": "}"}  # 压栈操作，遇到某种左括号，则压入其对应的右括号
        # if s[0] not in h_press:  # 如果s首个符号就不具备压栈条件，返回False(与21行代码等效，可省略)
        #     return False
        stack = list()  # 空栈
        for i in s:
            if i in h_press:  # 具备压栈条件
                stack.append(h_press[i])  # 压入对应右括号
            elif i in h_press.values():  # 具备弹栈条件
                if len(stack) == 0 or stack.pop() != i:  # 如果空栈或弹栈操作与栈顶操作不一致
                    return False
        if stack:  # 遍历s后不为空栈
            return False
        else:
            return True
```
