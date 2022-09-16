"""
国际leetcode网站题目：https://leetcode.com/problems/reverse-nodes-in-k-group/

Description:
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_positon=None):
        self.val = val
        self.next = next_positon


class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # 提交答案部分从此开始
        start = head
        end = self.getGroupEnd(k, start)
        if end is None:  # 如果整条链表长度<k，根据题意，不做翻转，返回原链表
            return head
        head = end  # 第一个group的尾，即新链表的头。那时，新链表head起始位置为这个end。
        self.reverse(start, end)  # 翻转group
        lastend = start  # 上一组的结尾，即start
        while lastend.next:
            start = lastend.next
            end = self.getGroupEnd(k, start)
            if end is None:
                return head
            self.reverse(start, end)
            lastend.next = end  # 因为group翻转，lastend所代表的的节点指针指向需要修正到group的新头end
            lastend = start  # lastend来到新的上一组的结尾
        return head

    def getGroupEnd(self, k, start):
        """
        寻找K个节点一组的头结点，如果数量不够返回空
        :param k: 组内节点数
        :param start: 起始位置
        :return: 新的start或者空
        """

        k -= 1
        while k and start:
            k -= 1
            start = start.next
        return start

    def reverse(self, start, end):
        end = end.next  # 记住group的下一个位置
        upstream = None
        cur = start
        downstream = None
        while cur != end:
            downstream = cur.next  # 记住当前的下一个位置
            cur.next = upstream  # 将当前指针翻转指向上游位置
            upstream = cur  # 当前位置标记下一个循环的为上游
            cur = downstream  # 下游位置标记为下一个循环的当前位置
        start.next = end  # start现在是翻转后的尾部，将其指针指向group的下一位置
