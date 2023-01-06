[2180. 统计各位数字之和为偶数的整数个数_cn-leetcode](https://leetcode.cn/problems/count-integers-with-even-digit-sum/description/)
<br>给你一个正整数<kbd>num</kbd> ，请你统计并返回 小于或等于<kbd>num</kbd>且各位数字之和为**偶数**的正整数的数目。
<br>正整数的**各位数字之和**是其所有位上的对应数字相加的结果。

**示例1**
>输入：
> <br>&emsp;&emsp;num = 4
>
>输出：
> <br>&emsp;&emsp;2
>
>解释：
> <br>&emsp;&emsp;只有 2 和 4 满足小于等于 4 且各位数字之和为偶数。

**示例2**
>输入：
> <br>&emsp;&emsp;num = 30
>
>输出：
> <br>&emsp;&emsp;14
>
>解释：
> <br>&emsp;&emsp;只有 14 个整数满足小于等于 30 且各位数字之和为偶数，分别是： 2、4、6、8、11、13、15、17、19、20、22、24、26 和 28 。

**提示**
<ul>
<li><kbd>1 <= num <= 1000</kbd></li>
</ul>

**核心代码模式【带对数器】**

```python3
import random


def countEven(num: int) -> int:
    """
    计算出不大于num且各位数字之和为偶数的正整数的数量

    思路：
    1位数符合要求的个数为：(9 - 0 + 1) // 2 = 5，但是0不算，故共5- 1 = 4个(也可以理解为4.5个取整为4个，规律更明显)
    2位数符合要求的个数为：(99 - 10 + 1) // 2 = 45个
    3位数符合要求的个数为：(999 - 100 + 1) // 2 = 450个
    ……
    我们得到规律：对于K位数，共有9 * (10 ** K)个数字，其中“一半”的数字满足要求，即[4.5 * (10 ** K)]个
    那么对于任意m位的正整数n，共有[4.5 * (10 ** (m - 1) - 1) / (10 - 1) - 0.5] + (n - (10 ** (m - 1))) // 2 + 1/0个
    第一项：(m - 1)项公比为10的等比数列求和，4.5作为首项，因此后面-0.5
    第二项：单求m位数从10**(m - 1)到n之前符合要求的个数
    第三项：1/0:debug时发现的修正项：如果自身为偶数且数字和为偶数则+1，否则+0

    :param num: 给定正整数
    :return: 所求正整数的个数
    """

    # 1. 求num的十进制位数
    digit = 0
    while 10 ** digit <= num:  # 不满足while循环时的digit值即为num的位数
        digit += 1

    # 2. 核验num本身性质
    digit_sum = 0
    for d in str(num):
        digit_sum += int(d)
    digit_sum = 1 if (((digit_sum & 1) ^ 1) and ((num & 1) ^ 1)) else 0  # 如果digit_sum为偶数且num为偶数，则赋值为1，否则赋值为0。

    # 3. 计算出不大于num且各位数字之和为偶数的正整数的数量
    return (num - (10 ** (digit - 1)) + 1) >> 1 if digit == 1 else (((10 ** (digit - 1) - 2) + (
            num - (10 ** (digit - 1))) + 1) >> 1) + digit_sum


def count(n: int) -> tuple:
    ans = 0
    ans_list = list()
    for i in range(1, n + 1):
        he = 0
        for h in str(i):
            he += int(h)
        if he % 2 == 0:
            ans += 1
            ans_list.append(i)
    return ans, ans_list


if __name__ == "__main__":
    for j in range(50000):
        test_num = random.randint(1, 100)
        right_ans, right_ans_list = count(test_num)
        my_ans = countEven(test_num)
        try_times = 0
        if right_ans != my_ans:
            print(f'NO.{try_times} failed: num:{test_num}, right answer is {right_ans}, my answer is {my_ans}\nans_list:{right_ans_list}')
            break
        else:
            try_times += 1
    print("Well Done !")
```
