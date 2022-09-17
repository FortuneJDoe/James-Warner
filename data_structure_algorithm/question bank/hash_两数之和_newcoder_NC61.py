"""
https://www.nowcoder.com/practice/20ef0972485e41019e39543e8e895b7f?tpId=117&&tqId=37756

描述：
给出一个整型数组 numbers 和一个目标值 target，请在数组中找出两个加起来等于目标值的数的下标，返回的下标按升序排列。
（注：返回的数组下标从1开始算起，保证target一定可以由数组里面2个数字相加得到）

数据范围：2≤ len(numbers) ≤ 10^5，-10 ≤ numbers_i ≤ 10^9，0 ≤ target ≤ 10^9
要求：空间复杂度 O(n)O(n)，时间复杂度 O(nlogn)O(nlogn)

Input:[3,2,4],6
Output:[2,3]
因为 2+4=6 ，而 2的下标为2 ， 4的下标为3 ，又因为 下标2 < 下标3 ，所以返回[2,3]

Input:[20,70,110,150],90
Output:[1,2]
20+70=90

"""
from typing import List


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可

# @param numbers int整型一维数组
# @param target int整型
# @return int整型一维数组

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []  # 答案列表
        h = dict()  # 哈希表
        for i in range(len(numbers)):  # 遍历数组
            difference = target - numbers[i]  # 计算结果与当前数的差
            if difference not in h:  # 如果差不在hash表的key中
                h[numbers[i]] = i + 1  # 将numbers[i]作为key,i+1做为value进到hash中
            else:  # 如果差值在hash的key中(说明这个差和当前值都在原数组中，且和为目标)
                res.append(h[difference])  # 差的索引更小，先记录进res中
                res.append(i + 1)  # 当前值索引压入队列
                break  # 跳出loop
        return res  # 返回答案
