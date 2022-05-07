class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = 0
        maxlength = 0
        d = dict()  # 记录字符下标
        for tail in range(0, len(s)):
            if s[tail] not in d:
                d[s[tail]] = tail  # 将不重复的元素的字符和对应的下标存入字典
            else:  # 出现重复元素
                pos = d[s[tail]] + 1  # 字典原中重复元素的下一个位置
                for i in range(head, pos):
                    d.pop(s[i])
                head = pos  # 将头指针指向重复元素的下一个位置
                d[s[tail]] = tail  # 修改字典重复元素的下标

            if (tail - head + 1) > maxlength:
                maxlength = tail - head + 1

        return maxlength



s1 = Solution()
s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s= ''
print(s1.lengthOfLongestSubstring(s))