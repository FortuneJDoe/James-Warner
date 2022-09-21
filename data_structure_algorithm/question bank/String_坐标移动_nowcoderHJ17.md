[HJ17 坐标移动 nowcoder](https://www.nowcoder.com/practice/119bcca3befb405fbe58abe9c532eb29?tpId=37&tqId=21240&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=)

开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
<br>输入：
<br>合法坐标为A(或者D或者W或者S) + 数字（两位以内）
<br>坐标之间以;分隔。
<br>非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。

<br>下面是一个简单的例子 如：
<br>A10;S20;W10;D30;X;A1A;B10A11;;A10;
<br>处理过程：
<br>起点（0,0）
<br>+   A10   =  （-10,0）
<br>+   S20   =  (-10,-20)
<br>+   W10  =  (-10,-10)
<br>+   D30  =  (20,-10)
<br>+   x    =  无效
<br>+   A1A   =  无效
<br>+   B10A11   =  无效
<br>+  一个空 不影响
<br>+   A10  =  (10,-10)

结果 （10， -10）

数据范围：每组输入的字符串长度满足 $1 \le n \le 10000$ ，坐标保证满足 $-2^{31} ≤ x,y ≤ 2^{31}-1$，且数字部分仅含正数
<br>输入描述： 一行字符串
<br>输出描述： 最终坐标，以逗号分隔

**示例1**
>输入： A10;S20;W10;D30;X;A1A;B10A11;;A10;
> 
>输出：10,-10

**示例2**
>输入： ABC;AKL;DA1;
> 
>输出：0,0

**ACM模式**


```python
import sys

for line in sys.stdin:
    a = line.strip("\n").split(";")
    h = {"A": (0, -1), "D": (0, 1), "W": (1, 1), "S": (1, -1)}
    initial = [0, 0]
    for i in a:
        if len(i) < 2 or len(i) > 3:
            continue
        if i[0] not in "WSAD" or i[1] not in "1234567890":
            continue
        if len(i) == 3 and (i[2] not in "1234567890"):
            continue
        initial[h[i[0]][0]] += h[i[0]][1] * int(i[1:])
    print(f"{initial[0]},{initial[1]}")
```
