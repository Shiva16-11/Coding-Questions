# Given a string s, return the longest palindromic substring in s

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start = 0
        end = 0

        for x in range(len(s)):
            l1 = expand(s, x, x)
            l2 = expand(s, x, x + 1)
            l = max(l1, l2)
            if l > (end - start):
                start = x - (l - 1) // 2
                end = x + l // 2
        return s[start: end + 1]

