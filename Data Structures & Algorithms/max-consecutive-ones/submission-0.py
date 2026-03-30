class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons = 0
        cons = 0
        for num in nums:
            if num == 1:
                cons += 1
                if cons > max_cons:
                    max_cons = cons
            else:
                cons = 0
        
        return max_cons
        