[901 股票价格跨度 cn-leetcode](https://leetcode.cn/problems/online-stock-span/)
<br>编写一个<kbd>StockSpanner</kbd>类，它收集某些股票的每日报价，并返回该股票当日价格的跨度
<br>今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续日数(从今天开始往回数，包括今天)
<br>例如，如果未来7天股票的价格是<kbd>[100, 80, 60, 70, 60, 75, 85]</kbd>，那么股票跨度将是<kbd>[1, 1, 1, 2, 1, 4, 6]</kbd>


**示例1**
>输入：
> <br>&emsp;&emsp;["StockSpanner","next","next","next","next","next","next","next"],
> <br>&emsp;&emsp;[[],[100],[80],[60],[70],[60],[75],[85]]
> 
>输出：
> <br>&emsp;&emsp;[null,1,1,1,2,1,4,6]
> 
>解释：
> <br>&emsp;&emsp;首先，初始化 S = StockSpanner()，然后：
> <br>&emsp;&emsp;S.next(100) 被调用并返回 1，
> <br>&emsp;&emsp;S.next(80) 被调用并返回 1，
> <br>&emsp;&emsp;S.next(60) 被调用并返回 1，
> <br>&emsp;&emsp;S.next(70) 被调用并返回 2，
> <br>&emsp;&emsp;S.next(60) 被调用并返回 1，
> <br>&emsp;&emsp;S.next(75) 被调用并返回 4，
> <br>&emsp;&emsp;S.next(85) 被调用并返回 6，
> <br>&emsp;&emsp;注意 (例如) S.next(75) 返回 4，因为截至今天的最后 4 个价格(包括今天的价格 75) 小于或等于今天的价格


**提示**
<ul>
<li>调用<kbd>StockSpanner.next(int price)</kbd>时，将有<kbd>1 <= price <= 10^5</kbd></li>
<li>每个测试用例最多可以调用<kbd>10000</kbd>次<kbd>StockSpanner.next</kbd></li>
<li>在所有测试用例中，最多调用<kbd>150000</kbd>次<kbd>StockSpanner.next</kbd></li>
<li>此问题的总时间限制减少了<kbd>50%</kbd></li>
</ul>

**核心代码模式**

```python
class StockSpanner:

    def __init__(self):
        """栈内元素为双元素元组(当日价格, 对应跨度)"""

        self.stack = []

    def next(self, price: int) -> int:
        """
        总体逻辑：
        1. 如果栈顶元素的股价高于今日报价或者空栈，则(今日报价, 跨度1)压入栈
        2. 如果栈顶元素的股价低于今日报价，栈顶元素弹出，其对应跨度加入到今日报价的跨度上，直到空栈或栈顶元素的股价高于今日报价，然后(今日报价, 跨度spanner)压入栈
        :param price: 今日报价
        :return: 今日跨度spanner
        """

        spanner = 1  # 初始今日跨度
        while self.stack and price >= self.stack[-1][0]:
            temp_spanner = self.stack.pop()[1]  # 记录栈顶元素的跨度
            spanner += temp_spanner  # 跨度累加更新
        self.stack.append((price, spanner))  # 压入(今日报价, 跨度spanner)
        return spanner


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
```