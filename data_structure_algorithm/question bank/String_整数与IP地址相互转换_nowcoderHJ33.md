[HJ33 整数与IP地址间的转换 nowcoder](https://www.nowcoder.com/practice/66ca0e28f90c42a196afd78cc9c496ea?tpId=37&tqId=21256&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=)

**原理**：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成 一个长整数。
<br>**举例**：一个ip地址为10.0.3.193

| 每段数字 | 相对应的二进制数 |
|:----:|:--------:|
|  10  | 00001010 |
|  0   | 00000000 |
|  3   | 00000011 |
| 193  | 11000001 |

组合起来即为：00001010 00000000 00000011 11000001
<br>转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

数据范围：保证输入的是合法的 IP 序列

**输入描述**
<ol>
<li>输入IP地址</li>
<li>输入10进制型的IP地址</li>
</ol>

**输出描述**
<ol>
<li>输出转换成10进制的IP地址</li>
<li>输出转换后的IP地址</li>
</ol>

**示例1**
>输入：
><br>&emsp;&emsp;10.0.3.193
><br>&emsp;&emsp;167969729
> 
>输出：
><br>&emsp;&emsp;167773121
><br>&emsp;&emsp;10.3.3.193

**ACM模式**

```python
import sys


def otob(s, num):
    """
    十进制转换成二进制字符串输出
    :param s: 输入字符串(每一位0~9)
    :param num: 按num位二进制输出
    :return: num位二进制字符串
    """
    s = int(s)
    ans = ""
    for ii in range(num):
        if (s >> (num - 1 - ii)) & 1 == 1:
            ans += "1"
        else:
            ans += "0"
    return ans


for line in sys.stdin:
    line = line.strip("\n")
    if "." in line:  # 输入是ip地址
        line = line.split(".")
        for i in range(len(line)):
            line[i] = otob(line[i], 8)
        line = int("".join(line), 2)
        print(line)
    else:  # 输入是转换后的ip地址
        line = otob(line, 32)
        res = []
        for i in range(4):
            res.append(str(int(line[8 * i: 8 * i + 8], 2)))
        print('.'.join(res))
```