import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap_max = [-n for n in nums]
    heapq.heapify(heap_max)
    result = []
    while heap_max:
        max_value = -heapq.heappop(heap_max)
        result.append(max_value)
    return result

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
