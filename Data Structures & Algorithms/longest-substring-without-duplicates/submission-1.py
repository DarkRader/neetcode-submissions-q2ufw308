class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # unique = []
        # res = 0
        # counter = 0

        # for char in s:
        #     if char in unique:
        #         counter = 1
        #         unique = []
        #         unique.append(char)
        #     else:
        #         unique.append(char)
        #         counter += 1
        #         res = max(res, counter)

        # return res
        unique = []
        l, r = 0, 0
        res = 0

        while r != len(s):
            if s[r] in unique:
                l += 1
                r = l
                unique = []
                unique.append(s[r])
            else:
                unique.append(s[r])
                res = max(res, r - l + 1)
            r += 1

        return res


        