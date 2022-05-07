"""
author:cpy
date:2022/5/6
src:https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []  # 记录子串
        max_length = 0  # 记录字串最大长度
        for i in range(len(s)):  # 遍历给定字符串，i的相当于滑动窗口的右指针
            """
            首先判断当前字符是否在lst中：
            1.如果不在lst中，则说明没有出现重复元素，直接将当前字符添加到lst中；
            2.如果在lst中，则说明有重复元素，需要从列表的第一个元素开始删除，直至删除掉重复元素，再将当前字符添加至lst中。
            将当前子串的长度与max_length对比，取最大值。
            """
            while s[i] in lst:  # 若右指针指向的元素在列表中，则从左指针0开始进行删除元素，直至删除掉右指针指定的元素（即删除掉重复元素）
                del lst[0]
            lst.append(s[i])
            # if max_length < len(lst): max_length = len(lst)
            max_length = max(max_length, len(lst))
        return max_length


s1 = Solution()
s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = ''
print(s1.lengthOfLongestSubstring(s))
