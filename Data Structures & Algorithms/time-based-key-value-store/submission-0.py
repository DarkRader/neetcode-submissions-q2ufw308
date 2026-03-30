from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        print(values)

        right_most = bisect.bisect_right(values, (timestamp, chr(255)))
        if right_most == 0:
            return ""

        return values[right_most - 1][1]
        
