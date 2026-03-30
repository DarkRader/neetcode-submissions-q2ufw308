class Solution:
    def maxArea(self, heights: List[int]) -> int:
        cur_max = 0
        i, z = 0, len(heights) - 1

        while i < z:
            min_of_two = min(heights[i], heights[z])
            candidate_max = (z - i) * min_of_two
            if candidate_max > cur_max:
                cur_max = candidate_max

            if heights[i] >= heights[z]:
                z -= 1
            else:
                i += 1

        # for i, a in enumerate(heights):
        #     z = i + 1

        #     while z != len(heights):
        #         min_of_two = min(heights[i], heights[z])
        #         candidate_max = (z - i) * min_of_two

        #         if candidate_max > cur_max:
        #             cur_max = candidate_max
        #         z += 1

        return cur_max
            