# problem:
# sort a list numbers with insert (swapping sequences..)
# from left to right, need to swap the numbers so that
# the array is sorted from beginning to the key position
from typing import List


def solution(nums: List[int]) -> List[int]:

    if len(nums) <= 1:
        return nums

    for i in range(1, len(nums)):
        j = i
        while nums[j] < nums[j - 1] and j > 0:
            # do a swap
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1

    return nums


if __name__ == "__main__":
    test_case = [6, 4, 3, 8, 1, 9, 0, 0, -1]
    print(solution(test_case))
