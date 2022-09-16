"""
https://leetcode.com/problems/merge-two-sorted-lists/submissions/

Description:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_p=None):
        self.val = val
        self.next = next_p


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None or list2 is None:
            return list2 if list1 else list1
        l = list1
        r = list2
        balance = lambda x, y: x if x.val <= y.val else y
        current = balance(l, r)  # 找到起始位置
        new_list = current  # 作为新链表头结点
        if l.val <= r.val:  # 更新遍历的头结点位置
            l = l.next
        else:
            r = r.next
        while l and r:
            current.next = balance(l, r)# 上个位置的指针指向新选出的节点
            current = current.next
            if l.val <= r.val:
                l = l.next
            else:
                r = r.next
        rest = lambda x, y: x if x else y  # 上述过程，l,r一定不是同时来到空的位置
        current.next = rest(l, r)
        return new_list


if __name__ == '__main__':
    l1 = ListNode(1)
    l12 = ListNode(2)
    l13 = ListNode(4)
    l2 = ListNode(1)
    l22 = ListNode(3)
    l23 = ListNode(4)
    l1.next = l12
    l12.next = l13
    l2.next = l22
    l22.next = l23
    k = Solution()
    nl = k.mergeTwoLists(l1, l2)
