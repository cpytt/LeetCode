"""
author:cpy
date:2022/5/6
src:https://leetcode-cn.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/


给你一个整数数组 arr 和两个整数 k 和 threshold 。
请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。

输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出：3
解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。

输入：arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
输出：6
解释：前 6 个长度为 3 的子数组平均值都大于 5 。注意平均值不是整数。
"""


class Solution:
    def numOfSubarrays(self, arr: list, k: int, threshold: int) -> int:
        total_threshold = threshold * k
        total = sum(arr[:k])
        num = 0
        if total >= total_threshold: num += 1
        n = len(arr)
        for i in range(k, n):
            total = total - arr[i - k] + arr[i]
            if total >= total_threshold: num += 1
        return num


s = Solution()
arr, k, threshold = [2, 2, 2, 2, 5, 5, 5, 8], 3, 4
arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5
print(s.numOfSubarrays(arr, k, threshold))
