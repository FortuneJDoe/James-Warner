[HJ 41 称砝码 nowcoder](https://www.nowcoder.com/practice/f9a4c19050fc477e9e27eb75f3bfd49c?tpId=37&tqId=21264&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=)
<br>现有n种砝码，重量互不相等，分别为 m1,m2,m3…mn；
<br>每种砝码对应的数量为x1,x2,x3...xn。
<br>现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。

注：称重重量包括 0

数据范围：1≤n≤10;   1≤m_i≤2000;  1≤x_i≤10

**输入描述**：
<br>对于每组测试数据：
<br>第一行：n --- 砝码的种数(范围[1,10])
<br>第二行：m1 m2 m3 ... mn --- 每种砝码的重量(范围[1,2000])
<br>第三行：x1 x2 x3 .... xn --- 每种砝码对应的数量(范围[1,10])

**输出描述**
<br>利用给定的砝码可以称出的不同的重量数

**示例1**
>输入：
> <br>&emsp;&emsp;2
> <br>&emsp;&emsp;1 2
> <br>&emsp;&emsp;2 1
> 
>输出：
> <br>&emsp;&emsp;5
> 
>解释：
> <br>&emsp;&emsp;可以表示出0，1，2，3，4五种重量

**ACM模式**

```python
n = int(input())
# mess = list(map(int,input().split()))
mess = [int(i) for i in input().split()]  # 测试用例中有结尾多一个space字符的，如果写成.split(' ')则末尾多一个''无法用int()转化而报错
num = list(map(int,input().split()))
bank = []  # 存放所有砝码
for i in range(n):
    for k in range(num[i]):
        bank.append(mess[i])
combination = {0, }  # 存放所有可测量质量，数据类型为set可以去重
for j in bank:
    for w in list(combination):  # 遍历所有现有组合(注意set会更新)
        combination.add(j + w)  # 不重复的组合会加入set
print(len(combination))
```
