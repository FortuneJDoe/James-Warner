[191 Number of 1 Bits leetcode](https://leetcode.com/problems/number-of-1-bits/)
<br>[191 位1的个数 cn-leetcode](https://leetcode.cn/problems/number-of-1-bits/)
<br>编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为[汉明重量](https://baike.baidu.com/item/%E6%B1%89%E6%98%8E%E9%87%8D%E9%87%8F)）

**特别提示**
<ul>
<li>请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。</li>
<li>在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3</li>
</ul>

**示例1**
>输入：
> <br>&emsp;&emsp;00000000000000000000000000001011
> 
>输出：
> <br>&emsp;&emsp;3
> 
>解释：
> <br>&emsp;&emsp;输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'

**示例2**
>输入：
> <br>&emsp;&emsp;00000000000000000000000010000000
> 
>输出：
> <br>&emsp;&emsp;1
> 
>解释：
> <br>&emsp;&emsp;输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'

**示例3**
>输入：
> <br>&emsp;&emsp;11111111111111111111111111111101
> 
>输出：
> <br>&emsp;&emsp;31
> 
>解释：
> <br>&emsp;&emsp;输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'

**提示**
<br>输入必须是长度为 32 的**二进制串**

**进阶**
<br>如果多次调用这个函数，你将如何优化你的算法？


**核心代码模式**

```python
class Solution:
    def hammingWeight(self, n):
        n = (n & (0x55555555)) + ((n >> 1) & (0x55555555))
        n = (n & (0x33333333)) + ((n >> 2) & (0x33333333))
        n = (n & (0x0f0f0f0f)) + ((n >> 4) & (0x0f0f0f0f))
        n = (n & (0x00ff00ff)) + ((n >> 8) & (0x00ff00ff))
        n = (n & (0x0000ffff)) + ((n >> 16) & (0x0000ffff))
        return n
```

**[高赞解答](https://leetcode.com/problems/number-of-1-bits/discuss/1044775/Python-n-and-(n-1)-trick-+-even-faster-explained)**&emsp;&emsp;[作者:DBabichev](https://leetcode.com/DBabichev/)

### just 5 operations
<br>&emsp;&emsp;You can stop on previous solution and interviewer will be OK with that. But if you show him the following solution, he will be really happy. Let us understand what is going on in the following code.
<ol>
<li>First of all <kbd>0x55555555 = 01010101010101010101010101010101</kbd> in binary representation, so first step will deal with even and odd bits. What happens after first line of code computed: it will count number of non-zero bits in each pair. For simplicity imagine just first <kbd>8</kbd> bits with constant <kbd>0x55 = 01010101</kbd> and choose <kbd>n = 11000110</kbd>, then we have is <kbd>10 00 01 01</kbd>. Why? We have <kbd>2</kbd>, that is <kbd>10</kbd> ones in first pair, than we have <kbd>0</kbd> ones, than we have <kbd>1</kbd> one and finally we also have <kbd>1</kbd>.</li>
<li>Now, to the second step, we have <kbd>0x33333333 = 110011001100110011001100110011</kbd>. Again let us look at only first <kbd>8</kbd> bit, that is to <kbd>11001100</kbd>. What will happend after this step, number of non-zero bits in groups of <kbd>4</kbd> will be computed. We stopped on number <kbd>10 00 01 01</kbd>, now we have <kbd>0010 0010</kbd>, because there is <kbd>2 + 0</kbd> ones in first group and <kbd>1 + 1</kbd> ones in second group.</li>
<li>Next step is <kbd>0x0f0f0f0f = 1111000011110000111100001111</kbd> and we're working with groups of <kbd>8</kbd>, so for our example we will have <kbd>00000100</kbd>, because we have <kbd>2</kbd> ones in each group.</li>
</ol>
<br>**Complexity**:we have only <kbd>5</kbd> iterations for <kbd>int32</kbd> number, it will be <kbd>6</kbd> for <kbd>int64</kbd>, <kbd>7</kbd> for <kbd>int128</kbd> and so on. For <kbd>int32</kbd> there will be not increase of speed, because even though it is <kbd>5</kbd> operations, each of them consists of several small steps, but for <kbd>int64</kbd> you can fill the difference. Space complexity is <kbd>O(1)</kbd>.