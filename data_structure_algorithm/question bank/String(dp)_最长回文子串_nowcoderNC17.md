[NC17 最长回文子串 nowcoder](https://www.nowcoder.com/practice/b4525d1d84934cf280439aeecc36f4af?tpId=196&tqId=37122&rp=1&ru=/exam/oj&qru=/exam/oj&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D196&difficulty=undefined&judgeStatus=undefined&tags=&title=)

对于长度为n的一个字符串A（仅包含数字，大小写英文字母），请设计一个高效算法，计算其中最长回文子串的长度。

数据范围：1≤n≤1000
<br>要求：空间复杂度 O(1)，时间复杂度 O(n^2)
<br>进阶: 空间复杂度 O(n)，时间复杂度 O(n)

**示例1**
>输入：
> <br>&emsp;&emsp;"ababc"
> 
>输出：
> <br>&emsp;&emsp;3
> 
>解释：
> <br>&emsp;&emsp; 最长的回文子串为"aba"与"bab"，长度都为3

**示例2**
>输入：
> <br>&emsp;&emsp;"abbba"
> 
>输出：
> <br>&emsp;&emsp;5

**示例3**
>输入：
> <br>&emsp;&emsp;"b"
> 
>输出：
> <br>&emsp;&emsp;1

**核心代码模式**

```python
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param A string字符串
# @return int整型
#
class Solution:
    def getLongestPalindrome(self, A: str) -> int:
        if A is None:  # 如果字符串空，则长度为0
            return 0
        max_length = 1  # 字符串不为空，最小回文子串长度为1，作为初始值
        for mx_len in range(2, len(A) + 1):  # 假设子串长度为[2, 字符串长]
            for l in range(len(A) + 1 - mx_len):  # 子串左起点[0, 字符串长 - 假设子串长]
                # r = l + mx_len - 1  # 提醒计算右边界不要超出范围
                if mx_len % 2 == 0:  # 假设子串长度为偶数
                    # A[起点:中点(靠左):][字符串逆序] == A[中点(靠右):终点:] 返回True，则回文子串判成
                    if A[l: l + (mx_len >> 1):][::-1] == A[(l + (mx_len >> 1)): l + mx_len:]:
                        max_length = max(max_length, mx_len)  # 更新最大长度
                        break # 该假设字串长度已经存在回文，跳出循环，假设子串长度+1
                    else:  # 返回False，跳出循环，更新左起点，继续判定
                        continue
                if mx_len % 2 == 1:  # 假设子串长度为奇数
                    # A[左起点:中点 + 1(不然取不到中点):][逆序] == A[中点:终点:] 返回True，则回文子串判成
                    if A[l: (l + (mx_len >> 1)) + 1:][::-1] == A[l + (mx_len >> 1): l + mx_len:]:
                        max_length = max(max_length, mx_len)  # 更新最大长度
                        break # 该假设字串长度已经存在回文，跳出循环，假设子串长度+1
                    else:  # 返回False，跳出循环，更新左起点，继续判定
                        continue
        return max_length
```
