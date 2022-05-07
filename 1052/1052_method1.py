"""
author:cpy
date:2022/5/7
src:https://leetcode-cn.com/problems/grumpy-bookstore-owner/


有一个书店老板，他的书店开了n分钟。每分钟都有一些顾客进入这家商店。给定一个长度为 n 的整数数组 customers ，其中 customers[i] 是在第 i 分钟开始时进入商店的顾客数量，所有这些顾客在第 i 分钟结束后离开。
在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。
当书店老板生气时，那一分钟的顾客就会不满意，若老板不生气则顾客是满意的。
书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续minutes分钟不生气，但却只能使用一次。

请你返回 这一天营业下来，最多有多少客户能够感到满意 。

示例1：
输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
输出：16
解释：书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.

示例2：
输入：customers = [1], grumpy = [0], minutes = 1
输出：1
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
            elif grumpy[i] == 1:
                F_satisfied += customers[i]

        max_sub = F_satisfied  # 记录滑动窗口中，不满意顾客的最大数量

        for j in range(k, n):
            """
            开始滑动窗口，更新记录 整个customer满意的顾客数 和 不满意顾客的最大数量
            """
            # 更新记录整个customer满意的顾客数
            if grumpy[j] == 0:
                T_satisfied += customers[j]
            # 更新当前窗口下，不满意的顾客数
            elif grumpy[j] == 1:
                F_satisfied += customers[j]
            if grumpy[j - k] == 1:
                F_satisfied -= customers[j - k]
            max_sub = max(F_satisfied, max_sub)  # 比较当前窗口下不满意的顾客数 和 不满意顾客的最大数量

        return max_sub + T_satisfied


s = Solution()
print(s.maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], minutes=3))
print(s.maxSatisfied(customers = [1], grumpy = [0], minutes = 1))