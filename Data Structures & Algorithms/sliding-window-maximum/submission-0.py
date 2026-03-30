class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        for l, num in enumerate(nums):
            if l + k - 1 == len(nums):
                break
            
            min_iter = float("-infinity")
            r = 0
            while r < k:
                if nums[l+r] > min_iter:
                    min_iter = nums[l+r]
                r += 1

            res.append(min_iter)

        return res


        