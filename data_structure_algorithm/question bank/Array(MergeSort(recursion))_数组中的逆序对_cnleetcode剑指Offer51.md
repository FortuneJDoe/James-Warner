[剑指Offer51 数组中的逆序对](https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/description/)
<br>&emsp;&emsp;题目描述: 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

<br>**示例1：**
>输入: [7,5,6,4]
>输出: 5

<br>**限制：**<kbd>0 <= 数组长度 <= 50000</kbd>

<br>**核心代码模式**
```python3
	class Solution:
	    def merge(self, arr, left, middle, right):
	        help_arr = []
	        p_1, p_2 = left, middle + 1
	        res = 0
	        while p_1 <= middle and p_2 <= right:
	            if arr[p_1] <= arr[p_2]:
	                help_arr.append(arr[p_2])
	                p_2 += 1
	            else:
	                res += right - p_2 + 1
	                help_arr.append(arr[p_1])
	                p_1 += 1
	        if p_1 <= middle:
	            help_arr.extend(arr[p_1: middle + 1])
	        if p_2 <= right:
	            help_arr.extend(arr[p_2: right + 1])
	        
	        i = 0
	        while i < len(help_arr):
	            arr[left + i] = help_arr[i]
	            i += 1
	        
	        return res
	 
	    def process(self, arr, left, right):
	        if left == right:
	            return 0
	        else:
	            mid = left + ((right - left) >> 1)
	            return self.process(arr, left, mid) + self.process(arr, mid + 1, right) + self.merge(arr, left, mid, right)
	 
	 
	    def reversePairs(self, nums: List[int]) -> int:
	        if not nums or len(nums) < 2:
	            return 0
	        else:
	            lf, rt = 0, len(nums) - 1
	            return self.process(nums, lf, rt)
```
