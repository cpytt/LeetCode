"""
author:cpy
date:2022/5/7
src:https://leetcode-cn.com/problems/grumpy-bookstore-owner/

主要取消了很多判断的部分。
"""


class Solution:
    def maxSatisfied(self, customers: list, grumpy: list, minutes: int) -> int:
        T_satisfied = 0  # 记录整个customer满意的顾客数
        F_satisfied = 0  # 记录当前滑动窗口内 不满意的顾客数，窗口长度固定：minutes
        k = minutes  # 滑动窗口的长度
        n = len(customers)  # customer长度

        for i in range(k):
            """
            记录初始的滑动窗口中 满意的顾客数 和 不满意的顾客数
            """
            if grumpy[i] == 0:
                T_satisfied += customers[i]
            F_satisfied += grumpy[i] * customers[i]

        max_sub = F_satisfied  # 记录滑动窗口中，不满意顾客的最大数量

        for j in range(k, n):
            """
            开始滑动窗口，更新记录 整个customer满意的顾客数 和 不满意顾客的最大数量
            """
            # 更新记录整个customer满意的顾客数
            if grumpy[j] == 0:
                T_satisfied += customers[j]
            # 更新当前窗口下，不满意的顾客数
            F_satisfied = F_satisfied + grumpy[j] * customers[j] - grumpy[j-k] * customers[j-k]
            max_sub = max(F_satisfied, max_sub)  # 比较当前窗口下不满意的顾客数 和 不满意顾客的最大数量

        return max_sub + T_satisfied


s = Solution()
print(s.maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], minutes=3))
print(s.maxSatisfied(customers = [1], grumpy = [0], minutes = 1))