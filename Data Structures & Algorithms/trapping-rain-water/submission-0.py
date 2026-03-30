class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        for i, a in enumerate(height):
            z = len(height) - 1 - i

            if i == 0:
                max_left[i] = 0
                max_right[-1] = 0
            else:
                new_left_max = max(height[i - 1], max_left[i - 1])
                max_left[i] = new_left_max

                new_right_max = max(height[z + 1], max_right[z + 1])
                max_right[z] = new_right_max

        for i, a in enumerate(height):
            res_op = min(max_left[i], max_right[i]) - a
            if res_op >= 0:
                res += res_op

        return res