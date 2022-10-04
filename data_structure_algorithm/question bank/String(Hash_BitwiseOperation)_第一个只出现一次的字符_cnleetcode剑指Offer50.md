[剑指Offer 50 第一个只出现一次的字符 cn-leetcode](https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/)
<br>在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

**示例1**
>输入：
> <br>&emsp;&emsp;s = "abaccdeff"
> 
>输出：
> <br>&emsp;&emsp;b

**示例2**
>输入：
> <br>&emsp;&emsp;s = "" 
> 
>输出：
> <br>&emsp;&emsp;' '

**核心代码模式**

```python
class Solution:
    def firstUniqChar(self, s: str) -> str:
        if len(s) == 0:  # 如果字符串为空
            return ' '
        else:  # 字符串不为空
            state, flag = 0, 0  # 缓存标记(int类型)：state表示遇到至少一次，flag表示至少两次
            # state和flag为(二进制下)最后26位做判断的数，最高位对应z，最低位对应a
            for w in s:  # 第一次遍历字符串
                temp = ord(w) - 97  # 计算ASC II码距离，确定位数(97 为小写字母a的ASC II值)
                if state & (1 << temp):  # 将1左移对应位数，判断state该位是否为1(1则代表记录过该字符，0则未记录过该字符)
                    flag |= (1 << temp)  # state该位为1，则表示遇到了第二次，那么flag进行按位或，记录该字符至少出现两次
                else:  # state该位为0，则表示未记录过，这是第一次遇到该字符
                    state |= (1 << temp)  # state进行按位或运算，更新该字符对应位置的状态
            for j in s:  # 重新遍历字符串
                x = ord(j) - 97  # 计算ASC II码距离，确定位数
                if flag & (1 << x):  # 如果按此位数右移，得到flag对应位置为1，则表示此字符出现至少2次
                    continue  # 跳过
                else:  # 此字符未出现超过1次
                    return j  # 返回找到字符(返回的是“第一个这样的字符”)
            # 然而上述情况得到返回值的前提是——字符串中确实有只出现过1次的字符
            return ' '  # 遍历结束也未找到出现1次的字符
```

以上参考官网题解C++版本位运算答案，作者：L-Sheng
<br>链接：https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/by-l-sheng-q8ph/

**官网参考答案**

Python 代码中的<kbd>not c in dic</kbd>整体为一个布尔值；<kbd>c in dic</kbd>为判断字典中是否含有键<kbd>c</kbd>

```python
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]: return c
        return ' '

```

作者：jyd
<br>链接：https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/mian-shi-ti-50-di-yi-ge-zhi-chu-xian-yi-ci-de-zi-3/
<br>来源：力扣（LeetCode）
<br>著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

需指明：
<ul>
<li>该方法可以修改后找到所有出现过1次的字符</li>
<li>python 3.6之后版本dict类型为有序(指键值对在内存中根据加入到字典中的时间顺序有序)，因此该方法第二次遍历无需遍历字符串，只需遍历键值对即可找到(如果存在)第一个只出现一次的字符。
</li>
</ul>


**修改后的代码**
```python
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v == 1:
                return k
        return ' '
```
