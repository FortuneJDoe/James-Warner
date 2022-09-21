[HJ20 密码验证合格程序 nowcoder](https://www.nowcoder.com/practice/184edec193864f0985ad2684fbc86841?tpId=37&tqId=21243&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=)

密码要求:
<ul>
<li>长度超过8位</li>
<li>包括大小写字母.数字.其它符号,以上四种至少三种</li>
<li>不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）</li>
</ul>
<br>数据范围：输入的字符串长度满足 1 ≤ n ≤ 100

**示例1**
>输入：
><br>&emsp;&emsp;021Abc9000
><br>&emsp;&emsp;021Abc9Abc1
><br>&emsp;&emsp;021ABC9000
><br>&emsp;&emsp;021$bc9000
> 
>输出：
><br>&emsp;&emsp;OK
><br>&emsp;&emsp;NG
><br>&emsp;&emsp;NG
><br>&emsp;&emsp;OK


**ACM模式**


```python
import sys

for line in sys.stdin:
    line = line.strip('\n')  # 去掉输入最后的换行符'\n'
    if len(line) <= 8:  # 如果长度<8，违反要求
        print("NG")  # 输出NG
        continue  # 跳转下一条密码
    h = dict()  # 空哈希表，验证是否存在非法重复子串
    mark = 1  # 标记是否存在重复子串的记录，未检出值为1，已检出记为0
    menu = [False, False, False, False]  # include_[upper, lower, digit, else]
    f = [line[0].isupper(), line[0].islower(), line[0].isdigit()]  # 第1个字符属于哪一类
    s = [line[1].isupper(), line[1].islower(), line[1].isdigit()]  # 第2个字符属于哪一类
    if f[0] or s[0]:  # 前两个字符存在大写字母
        menu[0] = True  # menu中upper位置状态变更为True
    if f[1] or s[1]:  # 前两个字符存在小写字母
        menu[1] = True  # menu中lower位置状态变更为True
    if f[2] or s[2]:  # 前两个字符存在数字
        menu[2] = True  # menu中digit位置状态变更为True
    if True not in f or True not in s:  # 如果前两位都不是上述类别，则归为else类
        menu[3] = True  # menu中else位置状态变更为True
    for i in range(2, len(line)):  # 从第三位向后继续遍历(仅一次)
        # 如果存在比三位更长的重复子串，那么它们同样可以被只检查三位重复子串的算法识别出
        if line[i - 2 : i + 1] not in h:  # 以i位置结尾的3位子字符串，如果不在哈希表中
            h[line[i - 2 : i + 1]] = 1  # 记录这个子串入哈希表
        else:  # 以i位置结尾的3位子字符串，如果在哈希表中，说明之前被记录过相同的子字符串
            print("NG")  # 违反要求，输出NG
            mark = 0  # 标记为0，说明已经检出长度>=3的重复子串
            break  # 跳出该条密码的遍历
        if menu[0] is False:  # 尚未检出密码中含有大写字母
            menu[0] = line[i].isupper()  # 检验第i位置密码是否为大写字母
        if menu[1] is False:  # 尚未检出密码中含有小写字母
            menu[1] = line[i].islower()  # 检验第i位置密码是否为小写字母
        if menu[2] is False:  # 尚未检出密码中含有数字
            menu[2] = line[i].isdigit()  # 检验第i位置密码是否为数字
        if menu[3] is False:  # 尚未检出密码中含有其他字符
            # 如果第i位置非大写字母、小写字母或数字，则为其他字符
            menu[3] = False if line[i].isupper() or line[i].islower() or line[i].isdigit() else True
    if mark:  # 如果到这一步仍未检出非法(长度>=3)的重复子串
        count = 0  # 计数密码中字符类别数量
        for i in menu:
            if i:
                count += 1
        if count >= 3:  # 字符类别数量满足要求
            print('OK')
        else:  # 字符类别数量不满足要求
            print('NG')
```