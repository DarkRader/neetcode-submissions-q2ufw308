from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    size = len(arr)
    i = 0
    new_arr = []
    while i < size:
        elem = arr.pop()
        new_arr.append(elem)
        i += 1
    return new_arr


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
