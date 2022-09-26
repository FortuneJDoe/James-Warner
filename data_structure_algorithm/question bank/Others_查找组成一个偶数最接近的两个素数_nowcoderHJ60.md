[HJ 60 查找组成一个偶数最接近的两个素数 nowcoder](https://www.nowcoder.com/practice/f8538f9ae3f1484fb137789dec6eedb9?tpId=37&tqId=21283&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D2%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=)

<br>任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况
<br>本题目要求输出组成指定偶数的两个素数差值最小的素数对

数据范围：4≤n≤1000

**输入描述**：
<br>输入一个大于2的偶数

**输出描述**
<br>从小到大输出两个素数

**示例1**
>输入：
> <br>&emsp;&emsp;20
> 
>输出：
> <br>&emsp;&emsp;7
> <br>&emsp;&emsp;13

**ACM模式**

```python
n = int(input())

def isprimenumber(x):
    """
    确认质数
    :param x:待确认的数
    :return:True or False
    """

    if x <= 1:
        return False
    if x == 2:
        return True
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:  # 能被除1和自身之外的数整除
                return False
        return True

for j in range(n >> 1, n):  # 从中间向两边遍历，遇到的第一组就是所求
    if isprimenumber(j) and isprimenumber(n - j):
        print(n - j)
        print(j)
        break
```
