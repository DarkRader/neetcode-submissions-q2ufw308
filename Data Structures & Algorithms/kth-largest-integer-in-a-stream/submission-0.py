import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        self.max_heap = max_heap
        self.k = k    

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, -val)
        temp = self.max_heap.copy()
        for _ in range(self.k - 1):
            heapq.heappop(temp)
        print(temp)
        return -temp[0]
