class Solution:
    def maxArea(self, heights: List[int]) -> int:
        cur_max = 0
        i, z = 0, len(heights) - 1

        while i < z:
            area = (z - i) * min(heights[i], heights[z])
            cur_max = max(cur_max, area)

            if heights[i] > heights[z]:
                z -= 1
            else:
                i += 1

        return cur_max
            