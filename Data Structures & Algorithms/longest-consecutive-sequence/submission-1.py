class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        count = 1
        biggest_count = 1
        prev_num = nums[0]

        for i, num in enumerate(nums):
            if i == 0 or num == prev_num:
                continue

            if num - 1 == prev_num:
                count += 1
            else:
                count = 1

            if count > biggest_count:
                biggest_count = count

            prev_num = num

        return biggest_count
        