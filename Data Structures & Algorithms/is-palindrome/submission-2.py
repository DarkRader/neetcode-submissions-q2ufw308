class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, t = 0, len(s) - 1

        while not s[i].isalnum():
            i += 1
            if i == len(s):
                return True

        while True:
            while not s[i].isalnum():
                i += 1
            while not s[t].isalnum():
                t -= 1

            if s[i].lower() != s[t].lower():
                return False

            i, t = i + 1, t - 1

            if i == t or i > t:
                return True

        