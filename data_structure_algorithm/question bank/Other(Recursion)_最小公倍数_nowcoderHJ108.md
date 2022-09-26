[HJ 108 最小公倍数 nowcoder](https://www.nowcoder.com/practice/22948c2cad484e0291350abad86136c3?tpId=37&tqId=21331&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D3%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=)
<br>正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值
<br>设计一个算法，求输入A和B的最小公倍数

数据范围：1≤a,b≤100000

**输入描述**：
<br>输入两个正整数A和B

**输出描述**
<br>输出A和B的最小公倍数

**示例1**
>输入：
> <br>&emsp;&emsp;5 7
> 
>输出：
> <br>&emsp;&emsp;35

![img_3.png](img_3.png)
<br>gcd的算法是根据Euclidean algorithm来的

**ACM模式**

```python
a, b = map(int, input().split())

def getgcb(x, y):
    """
    求两个正整数的最大公约数，根据Euclidean algorithm(中文对应为“更相减损法”)
    :param x: 较大的数
    :param y: 较小的数
    :return: 最大公约数
    """
    if x % y == 0:  # 如果能整除
        return y  # 较小数就是最大公约数
    else:  # 如果不能整除
        return getgcb(y, x % y)  # 递归将被除数、除数和余数中较小的两个数按大小顺序递归(肯定是余数最小，除数第二小)


val = getgcb(max(a, b), min(a, b))
print(a * b // val)  # 两数之积，除以最大公约数，即为最小公倍数
```
