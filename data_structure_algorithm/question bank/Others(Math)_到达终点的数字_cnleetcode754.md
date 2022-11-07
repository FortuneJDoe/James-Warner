[754 到达终点数字 cn-leetcode](https://leetcode.cn/problems/reach-a-number/description/)
<br>在一根无限长的数轴上，你站在<kbd>0</kbd>的位置。终点在<kbd>target</kbd>的位置
<br>你可以做一些数量的移动<kbd>numMoves</kbd>:
<ul>
<li>每次你可以选择向左或向右移动</li>
<li>第<kbd>i</kbd>次移动(从<kbd>i==1</kbd>开始，到<kbd>i==numMoves</kbd>)，在选择的方向上走<kbd>i</kbd>步</li>
</ul>

给定整数<kbd>target</kbd>，返回*到达目标所需的* **最小** 移动次数(即最小<kbd>numMoves</kbd>)

**示例1**
>输入：
> <br>&emsp;&emsp;target = 2
> 
>输出：
> <br>&emsp;&emsp;3
> 
>解释：
> <br>&emsp;&emsp;第一次移动，从 0 到 1 
> <br>&emsp;&emsp;第二次移动，从 1 到 -1 
> <br>&emsp;&emsp;第三次移动，从 -1 到 2 

**示例2**
>输入：
> <br>&emsp;&emsp;target = 3
> 
>输出：
> <br>&emsp;&emsp;2
> 
>解释：
> <br>&emsp;&emsp;第一次移动，从 0 到 1 
> <br>&emsp;&emsp;第二次移动，从 1 到 3

**提示**
<ul>
<li><kbd>-10^9 <= target <= 10^9</kbd></li>
<li><kbd>target != 0</kbd></li>
</ul>

**核心代码模式**

```python3
from math import sqrt

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)  # 根据对称性，对target取绝对值
        n = int((-1 + sqrt(1 + 8 * target)) / 2)  # 根据求根公式求得当前n
        d = (n * (n + 1) >> 1) - target  # 计算delta
        if d == 0:  # 如果delta = 0
            return n  # 当前n为所求
        else:  # 如果delta < 0
            n += 1  # n++
            d += n  # 更新delta，此时delta > 0
            # delta为偶数则返回当前n，否则返回一个可以令delta为偶数的最小n
            return n + 1 + n % 2 if d & 1 else n
```

```cpp
// @子不语 发布在https://leetcode.cn/problems/reach-a-number/solutions/1946020/dao-da-zhong-dian-shu-zi-by-leetcode-sol-ak90/comments/1820961
class Solution {
public:
    int reachNumber(int target) {
        target = abs(target);
        int n = (-1 + sqrt(1 + 8.0 * target)) / 2;
        int d = target - n * (n + 1) / 2;
        if (!d) return n;
        d -= ++n;
        return (d & 1 ? n + 1 + n % 2 : n);
    }   
};
```

### 特别说明
&emsp;&emsp;首先感谢 @子不语 大佬发布的一元二次方程代码实现的启发。题解链接：[子不语-754. 到达终点数字](https://leetcode.cn/problems/reach-a-number/solutions/1946020/dao-da-zhong-dian-shu-zi-by-leetcode-sol-ak90/comments/1820961)
<br>&emsp;&emsp;本文侧重梳理如何由官方题解的时间复杂度为 $O(|target|)$ 循环迭代方法向时间复杂度为 $O(1)$ 的一元二次方程方法的思路、流程的转化。
<br>&emsp;&emsp;此外还对官方题解中一些省略的、自己有疑问的问题给出了证明过程。

### 一、基础设定：
&emsp;&emsp;定义自然数的前 $n$ 项和：**$S_{n}= \frac{n(n+1)}{2}$**
<br>&emsp;&emsp;同时定义： $S_{0}= 0$
<br>&emsp;&emsp;设：**$delta=S_{n}-target= \frac{n(n+1)}{2}-target$**

### 二、解题思路【循环迭代】：
当 $S_{n}$ 从 $n=0$ ~ $n$ 迭代过程中，

1. 找到一个最小的 $𝑛$ ，使得满足 $S_{n}=target$
2. 找到一个最小的 $𝑛$ ，使得满足 $delta=S_{n}−target>0$ 且 $𝑑𝑒𝑙𝑡𝑎$ 恰好是 $0$ ~ $𝑛$ 中的某几个数字之和的2倍

### 三、规律探索：
&emsp;&emsp;毫无疑问，遍历过程中 $delta$ 的值必先 $<0$ ，最终可能遇到 $=0$ ，也可能遇到 $>0$ 。

① $delta$ 由 $<0$ 到 $=0$ ：即等价于 $target$ 恰好为某个前 $n$ 项和 $S_{n}$
循环迭代过程如下图： $(target=10)$

1. $n=0$ ， $delta=S_{0}-10=-10$
2. $n=1$ ， $delta=S_{1}-10=1-10=-9$
3. $n=2$ ， $delta=S_{2}-10=3-10=-7$
4. $n=3$ ， $delta=S_{3}-10=6-10=-4$
5. $n=4$ ， $delta=S_{4}-10=10-10=0$ ，第1、2、3和4步均正向走即可

![image](https://user-images.githubusercontent.com/92873873/200305426-e94b36cf-777b-45fe-980d-5d0b0002277d.png)

② $delta$ 由 $<0$ 到 $>0$ ：
循环迭代过程如下图： $(target=14)$

1. $n=0$ ， $delta=S_{0}-14=-14$
2. $n=1$ ， $delta=S_{1}-14=1-14=-13$
3. $n=2$ ， $delta=S_{2}-14=3-14=-11$
4. $n=3$ ， $delta=S_{3}-14=6-14=-8$
5. $n=4$ ， $delta=S_{4}-14=10-14=-4$
6. $n=5$ ， $delta=S_{5}-14=15-14=1$ ； $\frac{delta}{2}=\frac{1}{2}=0.5$ 不是整数， $pass$
7. $n=6$ ， $delta=S_{6}-14=21-14=7$ ； $\frac{delta}{2}=\frac{7}{2}=3.5$ 不是整数， $pass$
8. $n=7$ ， $delta=S_{7}-14=28-14=14$ ； $\frac{delta}{2}=\frac{14}{2}=7$ ，前6步正向走，第7步负向走(也可以理解和为7的第16/25/34步负向走，其它步正向走)

![image](https://user-images.githubusercontent.com/92873873/200305502-56dd588f-a421-473e-a46c-2d7d2c5e0bb5.png)

&emsp;&emsp;上述过程可以做如下总结：

<kbd>1</kbd> 初始 $n=0$ 时，必有 $delta=S_{0}-target<0$ ，则需要 $n$ 依次增加；

<kbd>2</kbd> 当 $n=N-1$ 时，仍有 $delta=S_{N}-target<0$ ，则继续 $n++$

<kbd>3</kbd> 当 $n=N$ 时，

&emsp;&emsp;<kbd>3.1</kbd> 如果 $delta=0$ ，则 $N$ 为所求；

&emsp;&emsp;<kbd>3.2</kbd> 如果 $delta>0$ ，如果 $delta$ 为偶数，则等于(或者和等于) $\frac{delta}{2}$ 的数字(或者若干数字)为负数即可

&emsp;&emsp;<kbd>3.3</kbd> 如果 $delta>0$ ，如果 $delta$ 为奇数且 $N$ 为偶数，则 $n=N+1$ 为所求，此时 $delta=S_{N+1}-target$ 为偶数。情况就与3.2相同

&emsp;&emsp;<kbd>3.4</kbd> 如果 $delta>0$ ，如果 $delta$ 为奇数且 $N$ 为奇数，则 $n=N+2$ 为所求，此时 $delta=S_{N+2}-target$ 为偶数。情况就与3.2相同

### 四、总结优化【向一元二次方程解法转化】：
&emsp;&emsp;显然如果算法是按照<kbd>1</kbd>→<kbd>2</kbd>→<kbd>3</kbd>流程，时间复杂度即为 $O(|target|)$ ；
<br>&emsp;&emsp;如果算法可以在第一步就从<kbd>2</kbd>开始，那么时间复杂度就可以变成 $O(1)$ ，这是我们追求的。
<br>&emsp;&emsp;观察 $delta=S_{n}-target= \frac{n(n+1)}{2}-target$ ，发现其是形式上的 $delta$ 关于 $n$ 的一元二次函数
<br>&emsp;&emsp;通过令 $delta(n)=0$ ，根据一元二次方程求根公式中较大根的情况 $n=\frac{-1 + \sqrt{1 + 8 \times target} }{2}$ (注意这里 $n$ 为 $int$ 类型，相当于对求根公式计算结果向下取整)。得到的 $n$ 或者满足3.1的情况直接求出 $n$ ，或者满足<kbd>2</kbd>→<kbd>3.2</kbd>/<kbd>3.3</kbd>/<kbd>3.4</kbd>的情况

### 五、一些讨论【自己想通的几个疑惑】：
#### 假设：当 $delta$ 为偶数时，必然存在 $1$ ~ $n$ 中某个数(某几个数的和)等于 $\frac{delta}{2}$ ？
&emsp;&emsp;当 $n=N$ 时，若满足 $S_{N} < target < S_{N+1}$ ，设： $k=-delta = target-S_{N}$ ，易得 $k \in [1,N-1]$

1. $k$ 为奇数， $N$ 为偶数。当 $n=N+1$ ， $delta=N+1-k$ 为偶数，且易得此时 $\frac{delta}{2}=\frac{N+1-k}{2}=\frac{n-k}{2} \le n$ ，即 $\exists \frac{n-k}{2} \in [1, n]$ 满足假设。
2. $k$ 为偶数， $N$ 为奇数。当 $n=N+1$ ， $delta=N+1-k$ 为偶数，且易得此时 $\frac{delta}{2}=\frac{N+1-k}{2}=\frac{n-k}{2} \le n$ ，即 $\exists \frac{n-k}{2} \in [1, n]$ 满足假设。
3. $k$ 为奇数， $N$ 为奇数。
	<br>3.1 当 $n=N+1$ ， $delta=N+1-k$ 为奇数，
	<br>3.2 当 $n=N+2$ ， $delta=2N+3-k$ 为偶数，此时 $\frac{delta}{2}=\frac{2N+3-k}{2}=\frac{n+(n-1)-k}{2}=n-\frac{1+k}{2} \le n$ ，即 $\exists \frac{n-k}{2} \in [1, n]$ 满足假设。
4. $k$ 为偶数， $N$ 为偶数。
	<br>4.1 当 $n=N+1$ ， $delta=N+1-k$ 为奇数，
	<br>4.2 当 $n=N+2$ ， $delta=2N+3-k$ 为奇数，
	<br>4.3 当 $n=N+3$ ， $delta=3N+6-k$ 为偶数，此时 $\frac{delta}{2}=\frac{3N+6-k}{2}=\frac{3n-3-k}{2}=n+\frac{n-3-k}{2}$ ，即 $\exists$ { $\frac{n-3-k}{2}, n$ } $\subseteq  [1, n]$ 满足假设。
	&emsp;&emsp;P.S. 证明 $\frac{n-3-k}{2} \in [1, n]$ ：
	<br>&emsp;&emsp; $\because k \in$ { $2, 4, \cdots, N-4, N-2$ } $\Leftrightarrow  k \in$ { $2, 4, \cdots, n-7, n-5$ }
	<br>&emsp;&emsp; $\therefore \frac{n-3-k}{2} \in$ { $1, 2, \cdots, \frac{n-3}{2}, \frac{n-1}{2}$ } $\subseteq  [1, n]$
  
  举一个 $k=2$ 的例子：
  
  ![image](https://user-images.githubusercontent.com/92873873/200305622-63b3bd81-e9b7-4a2c-ab90-90a9e0fde6a6.png)
