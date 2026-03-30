class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict_nums = {}
        
        for num in nums:
            if not num in dict_nums:
                dict_nums[num] = 1
            else:
                return num


        return -1