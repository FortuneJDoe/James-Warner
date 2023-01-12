[NC37 合并空间 nowcoder](https://www.nowcoder.com/practice/69f4e5b7ad284a478777cb2a17fb5e6a?tpId=117&tqId=37737&rp=1&ru=/exam/oj&qru=/exam/oj&sourceUrl=%2Fexam%2Foj%3Fpage%3D5%26pageSize%3D50%26search%3D%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D117&difficulty=undefined&judgeStatus=undefined&tags=&title=)

给出一组区间，请合并所有重叠的区间。
<br>请保证合并后的区间按区间起点升序排列。

数据范围：区间组数 0≤n≤2×10^5 区间内的值都满足0≤val≤2×10^5
<br>要求：空间复杂度 O(n)，时间复杂度 O(nlogn)
<br>进阶：空间复杂度 O(val)，时间复杂度 O(val)

**示例1**
>输入：
><br>&emsp;&emsp;[[10,30],[20,60],[80,100],[150,180]]
> 
>返回值：
><br>&emsp;&emsp;[[10,60],[80,100],[150,180]]

**示例2**
>输入：
><br>&emsp;&emsp;[[0,10],[10,20]]
> 
>返回值：
><br>&emsp;&emsp;[[0,20]]

**核心代码模式**

```python
class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param intervals Interval类一维数组
# @return Interval类一维数组
#
from typing import List


class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if intervals:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        res = list()
        temp = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i].start <= temp.end:
                temp.end = max(intervals[i].end, temp.end)
            else:
                res.append(temp)
                temp = intervals[i]
        res.append(temp)
        return res
```
