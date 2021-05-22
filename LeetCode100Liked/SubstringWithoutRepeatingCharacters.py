# Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l == 0:
            return l
        x = 0
        ans = 0
        c = 0
        db = {}
        while x < l:

            if s[x] not in db:

                c += 1
                db[s[x]] = x
            else:
                ans = max(ans, c)
                c = 0
                x = db[s[x]]
                db = {}
            x += 1
        ans = max(ans, c)
        return ans

