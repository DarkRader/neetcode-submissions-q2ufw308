class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]

        while l < r:
            if max_left < max_right:
                l += 1
                res_op = max_left - height[l]
                if res_op >= 0:
                    res += res_op
                max_left = max(max_left, height[l])
            else:
                r -= 1
                res_op = max_right - height[r]
                if res_op >= 0:
                    res += res_op
                max_right = max(max_right, height[r])

        return res