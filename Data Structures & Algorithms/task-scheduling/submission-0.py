class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [ c for c in count.values() ]
        heapq.heapify_max(max_heap)
        queue = deque()
        time = 0

        while max_heap or queue:
            time += 1
            if max_heap:
                curr_count = heapq.heappop_max(max_heap)
                if curr_count - 1 > 0:
                    queue.append((curr_count - 1, time + n))

            if queue and queue[0][1] == time:
                num = queue.popleft()
                heapq.heappush_max(max_heap, num[0])

        return time
        