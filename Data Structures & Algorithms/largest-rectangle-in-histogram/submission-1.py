class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0

        for i, a in enumerate(heights):
            if a > res:
                res = a
            if i == len(heights) - 1:
                break
            z = i + 1
            cur_min = min(a, heights[z])
            wight = 2
            while z != len(heights):
                cur_min = min(cur_min, heights[z])
                print(cur_min)
                res_op = wight * cur_min
                if res_op > res:
                    print(i)
                    print(z)
                    res = res_op
                    print(res)
                wight += 1
                z += 1
                print("---------------")
        
        return res
        