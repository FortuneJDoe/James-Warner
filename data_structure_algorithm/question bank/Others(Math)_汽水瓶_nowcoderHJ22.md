[HJ22 汽水瓶 nowcoder](https://www.nowcoder.com/practice/fe298c55694f4ed39e256170ff2c205f?tpId=37&tqId=21245&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=)

**描述**
<br>&emsp;&emsp;某商店规定：三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶(但是必须要归还)。
<br>&emsp;&emsp;小张手上有n个空汽水瓶，她想知道自己最多可以喝到多少瓶汽水。
<br>&emsp;&emsp;数据范围: 输入的字符串长度满足 1≤n≤100

<br>注意：本题存在多组输入。输入的 0 表示输入结束，并不用输出结果。

**输入描述**
<br>输入文件最多包含 10 组测试数据，每个数据占一行，仅包含一个正整数 n(1<=n<=100)，表示小张手上的空汽水瓶数。n=0 表示输入结束，你的程序不应当处理这一行。

**输出描述**
<br>对于每组测试数据，输出一行，表示最多可以喝的汽水瓶数。如果一瓶也喝不到，输出0。

**示例1**
>输入：
> <br>&emsp;&emsp;3
> <br>&emsp;&emsp;10
> <br>&emsp;&emsp;81
> <br>&emsp;&emsp;0
> 
>输出：
> <br>&emsp;&emsp;1
> <br>&emsp;&emsp;5
> <br>&emsp;&emsp;40
> 
>说明：
> <br>&emsp;&emsp;样例 1 解释：用三个空瓶换一瓶汽水，剩一个空瓶无法继续交换
> <br>&emsp;&emsp;样例 2 解释：用九个空瓶换三瓶汽水，剩四个空瓶再用三个空瓶换一瓶汽水，剩两个空瓶，向老板借一个空瓶再用三个空瓶换一瓶汽水喝完得一个空瓶还给老板。


**ACM模式**

```python
import sys

for line in sys.stdin:
    line = int(line)
    if line:
        print(line // 2)
```