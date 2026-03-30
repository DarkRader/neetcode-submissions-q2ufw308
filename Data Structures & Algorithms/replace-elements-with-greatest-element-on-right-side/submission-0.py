class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for i, num in enumerate(arr):
            print(f"i: {i}, num: {num}")
            biggest = -1
            for j in range(i + 1, len(arr)):
                print(f"num_in: {arr[j]}")
                if arr[j] > biggest:
                    biggest = arr[j]
                    arr[i] = arr[j]
        arr[-1] = -1
        return arr


        