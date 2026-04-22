class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones] 
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            biggest = heapq.heappop(max_heap)
            second_biggest = heapq.heappop(max_heap)

            if biggest < second_biggest:
                heapq.heappush(max_heap, biggest - second_biggest)

        if max_heap:
            return -max_heap[0]
        return 0  
        