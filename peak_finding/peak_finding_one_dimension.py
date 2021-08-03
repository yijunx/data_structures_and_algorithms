# problem:
# given nums array, postion x is a peak <=> nums[x] >= nums[x-1] && nums[x] >= nums[x+1]
# for the edges, only need to be greater or equal to one side
# find a peak if it exists
from typing import List


def solution(nums: List[int]) -> int:
    if not nums:
        return

    n = len(nums)
    mid = n // 2
    if n == 1:
        return nums[0]

    if n == 2:
        return max(nums[0], nums[1])

    if nums[mid] < nums[mid - 1]:
        # the number at lhs is bigger, thus there will be a peak at the left half
        return solution(nums[:mid])
    elif nums[mid] < nums[mid + 1]:
        # the number at rhs is bigger, thus there will be a peak at the right half
        return solution(nums[mid + 1 :])
    else:
        return nums[mid]


if __name__ == "__main__":
    test_case = [1, 2, 3, 4, 5, 4, 1]
    print(solution(test_case))
