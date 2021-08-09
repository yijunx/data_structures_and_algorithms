# problem:
# sort a list numbers with insert (swapping sequences..)
# but this is merge sort
# merge sort applies divide and conquer algo, recursive
# it keeps breaking the problem into 2
# then the sort happens at merge at bottom where each portion has only one element
from typing import List


def merge(nums1: List[int], nums2: List[int]) -> List[int]:
    # num1 and num2 must be sorted before hand
    # one side is empty
    if not nums1:
        return nums2
    if not nums2:
        return nums1
    # well now both side not empty
    # use a two-finger method
    key1 = 0
    key2 = 0
    len1 = len(nums1)
    len2 = len(nums2)
    sorted = []
    while key1 + key2 < len1 + len2:
        if key1 == len1:
            sorted.append(nums2[key2])
            key2 += 1
        elif key2 == len2:
            sorted.append(nums1[key1])
            key1 += 1
        else:
            if nums1[key1] < nums2[key2]:
                sorted.append(nums1[key1])
                key1 += 1
            else:
                sorted.append(nums2[key2])
                key2 += 1
    return sorted


def solution(nums: List[int]) -> List[int]:

    if len(nums) <= 1:
        return nums

    left__part = nums[: len(nums) // 2]
    right_part = nums[len(nums) // 2 :]

    sorted_left__part = solution(left__part)
    sorted_right_part = solution(right_part)

    return merge(sorted_left__part, sorted_right_part)


if __name__ == "__main__":
    test_case = [6, 4, 3, 8, 1, 9, 0, 0, -1, 11, -21, 12, 3, 5]
    print(solution(test_case))
    # test_merge1 = [1,2,6]
    # test_merge2 = [2,3,8]
    # print(merge(test_merge1, test_merge2))
