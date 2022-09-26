[NC28 最小覆盖子串 nowcoder](https://www.nowcoder.com/practice/c466d480d20c4c7c9d322d12ca7955ac?tpId=196&tqId=37066&rp=1&ru=/exam/oj&qru=/exam/oj&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D196&difficulty=undefined&judgeStatus=undefined&tags=&title=)

给出两个字符串 s 和 t，要求在 s 中找出最短的包含 t 中所有字符的连续子串。

数据范围：1≤|S|,|T|≤10000，保证s和t字符串中仅包含大小写英文字母
<br>进阶: 空间复杂度 O(n)，时间复杂度 O(n)

**注意**：
<br>如果 s 中没有包含 t 中所有字符的子串，返回空字符串 “”；
<br>满足条件的子串可能有很多，但是题目保证满足条件的最短的子串唯一。

**示例1**
>输入：
> <br>&emsp;&emsp;"XDOYEZODEYXNZ","XYZ"
> 
>输出：
> <br>&emsp;&emsp;"YXNZ"

**示例2**
>输入：
> <br>&emsp;&emsp;"abcAbA","AA"
> 
>输出：
> <br>&emsp;&emsp;"AbA"

**核心代码模式**

```python
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param S string字符串 
# @param T string字符串 
# @return string字符串
#
class Solution:
    def checkmydict(self, dictionary):
        """
        检查字典中的值是否均<=0(成立则表示子串已形成)
        :param dictionary: 输入字典
        :return:布尔类型，所有值均<=0时返回False，至少有一个不为0返回True
        """
        
        for v in dictionary.values():
            if v > 0:
                return True
        return False
    
    def minWindow(self , S: str, T: str) -> str:
        last = -1  # 标记滑动窗口左边界的上一位，初始值-1
        res = []   # 记录所有满足条件的最小窗口
        h = dict()  # 辅助哈希表，记录窗口内需要满足的各个字符个数
        # 制作辅助哈希表
        for key in T:
            if key in h:
                h[key] += 1
            else:
                h[key] = 1
        # print(h)
        for r in range(len(S)):  # 移动右边界
            if S[r] in h:  # 遇到符合条件字符
                h[S[r]] -= 1  # 更新哈希表
                if self.checkmydict(h):  # 检查是否形成符合要求的子串，True表示未形成，False表示已形成
                    continue
                else:  # 已形成子串，下面求最小窗口
                    for l in range(last + 1, r + 1):  # 从[上一个l的后一个位置, r + 1]缩小串口
                        if S[l] in h:  # 遇到可能影响子串完整性的字符
                            h[S[l]] += 1  # 更新哈希表
                            if h[S[l]] > 0:  # 判断该字符是否不足？如果不足，则证明l来到该子串的最大左边界
                                res.append(S[l: r + 1:])  # 记录该子串
                                last = l  # 更新last
                                break  # 已找到该子串的最小窗口，不需要继续操作，跳出循环
                            else:  # 如果子串仍然满足，继续缩小窗口
                                continue
        # print(f'res={res}')
        if len(res) == 0:  # 如果res未记录任何子串，证明没有符合要求的子串
            return ''
        else:  # 如果res记录有子串
            res = sorted(res, key=lambda x: len(x))  # 按照子串长度升序排列
            return res[0]  # 返回最短子串(依据题意，最小子串只有一个)

```
