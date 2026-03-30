class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l_list, r_list = 0, len(matrix) - 1
        nums = []
        while l_list <= r_list:
            middle = (l_list + r_list) // 2
            if matrix[middle][-1] < target:
                l_list = middle + 1
            elif matrix[middle][0] > target:
                r_list = middle - 1
            else:
                nums = matrix[middle]
                break

        print(nums)

        l, r = 0, len(nums) - 1
        while l <= r:
            middle = (l + r) // 2
            if nums[middle] < target:
                l = middle + 1
            elif nums[middle] > target:
                r = middle - 1
            else:
                return True

        return False