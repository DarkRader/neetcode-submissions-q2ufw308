class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        cand_list = []

        cand_list = self.append_to_list(nums1, cand_list)
        cand_list = self.append_to_list(nums2, cand_list)

        cand_list.sort()
        print(cand_list)
        mid = (0 + len(cand_list) - 1) // 2
        if len(cand_list) % 2 == 0:
            return (cand_list[mid] + cand_list[mid + 1]) / 2

        return cand_list[mid]

    def append_to_list(self, nums_list: List[int], cand_list: List[int]) -> List[int]:
        if len(nums_list) == 0:
            return cand_list

        mid = (0 + len(nums_list) - 1) // 2
        cand_list.append(nums_list[mid])
        if len(nums_list) % 2 == 0:
            cand_list.append(nums_list[mid + 1])

        return cand_list
        