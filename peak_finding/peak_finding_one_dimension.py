# problem:
# given nums array, postion x is a peak <=> nums[x] >= nums[x-1] && nums[x] >= nums[x+1]
# for the edges, only need to be greater or equal to one side
# find a peak if it exists
from typing import List


def solution(nums: List[int]) -> int:
    if not nums:
        return
    
    n = len(nums)
    if n == 1:
        return nums[0]

    # recursively divide and conquer
    if nums[n // 2] >= nums[n-1] and nums[n // 2] >= nums[0]
    return


if __name__ == "__main__":
    test_case = []
    print(solution(test_case))