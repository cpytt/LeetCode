"""
author:cpy
date:2022/5/6
src:https://leetcode-cn.com/problems/maximum-average-subarray-i/
"""


class Solution:
    def findMaxAverage(self, nums: list, k: int) -> float:
        """
        计算固定窗口的平均数可以转化成求总和
        当前总和total = 左边减一个 右边加一个 加上原来总和
        """
        total = max_total = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            total = total - nums[i - k] + nums[i]
            max_total = max(total, max_total)

        return max_total / k


s = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(s.findMaxAverage(nums, k))
