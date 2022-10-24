# 无重复字符的最长子串
# 给定一个字符串 s ,请你找出其中不含有重复字符的最长子串的长度。
# 示例1:
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc",所以其长度为 3
class Solution3:
    def lengthOfLongestSubstring(self, s) -> int:
        """
        :type s: str
        :rtype: int
        """
        # 哈希集合记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针初始值为 -1相当于我们在字符串的左边界的左侧还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans
