# problem:
# find a peak in a 2d array where its value is
# greater or equal to its upper/left/right/down
from typing import List


def solution(nums: List[List[int]]) -> int:
    n = len(nums)
    m = len(nums[0])

    mid_col = m // 2
    mid_col_max = nums[0][m // 2]
    print(f"initial mid col max: {mid_col_max}")
    mid_col_max_idx = 0
    for i in range(n):
        if nums[i][mid_col] > mid_col_max:
            mid_col_max_idx = i
            mid_col_max = nums[i][mid_col]
    print(f"but the best guy is at location: {mid_col_max_idx}")
    # now we have the mid_col_max_idx
    # the strategy is, check its left and right neigbor
    # if the right neigher is higher, then we reduce the problem to the right half
    # ....... left ......................................................left ....
    # if neigher, then here is the peak!

    if m == 1:
        return mid_col_max

    if m == 2:
        return max(nums[mid_col_max_idx][0], nums[mid_col_max_idx][1])

    if nums[mid_col_max_idx][mid_col] < nums[mid_col_max_idx][mid_col + 1]:
        return solution([x[mid_col + 1 :] for x in nums])

    elif nums[mid_col_max_idx][mid_col] < nums[mid_col_max_idx][mid_col - 1]:
        return solution([x[:mid_col] for x in nums])

    else:
        return mid_col_max


if __name__ == "__main__":
    test_case = [
        [1, 2, 3, 4, 5, 0, 4, 1, 3, 4, 5],
        [4, 3, 2, 1, 5, 6, 9, 2, 3, 4, 0],
        [4, 5, 3, 2, 5, 4, 1, 4, 5, 5, 1],
        [8, 0, 1, 2, 5, 3, 5, 4, 5, 2, 9],
    ]
    print(solution(test_case))
