class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones] 
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            biggest = heapq.heappop(max_heap)
            second_biggest = heapq.heappop(max_heap)

            result = 0
            if biggest < second_biggest:
                result = biggest - second_biggest
                heapq.heappush(max_heap, result)

        if max_heap:
            return -max_heap[0]
        return 0
        
        