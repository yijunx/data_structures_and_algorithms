# problem:
from typing import List


def left(num: int):
    return 2 * num + 1


def right(num: int):
    return 2 * num + 2


def maxHeapifyList(nums: List[int], current_root: int = 0) -> List[int]:

    try:  # if it has right side, it sure has left side
        _ = nums[right(current_root)]
        # now there is left side and right side do both side!
        if (
            nums[left(current_root)] > nums[current_root]
            and nums[left(current_root)] > nums[right(current_root)]
        ):
            # swap left
            nums[left(current_root)], nums[current_root] = (
                nums[current_root],
                nums[left(current_root)],
            )
            # keep heafigy
            nums = maxHeapifyList(nums, current_root=left(current_root))
            return nums
        elif (
            nums[right(current_root)] > nums[current_root]
            and nums[right(current_root)] > nums[left(current_root)]
        ):
            # swap left
            nums[right(current_root)], nums[current_root] = (
                nums[current_root],
                nums[right(current_root)],
            )
            # keep heapigy
            nums = maxHeapifyList(nums, current_root=right(current_root))
            return nums
        else:
            return nums
    except:
        try:  # no right side...
            _ = nums[left(current_root)]
            # do one side
            if nums[left(current_root)] > nums[current_root]:
                # swap left
                nums[left(current_root)], nums[current_root] = (
                    nums[current_root],
                    nums[left(current_root)],
                )
                # keep heapigy
                nums = maxHeapifyList(nums, current_root=left(current_root))
                return nums
            else:
                return nums
        except:
            return nums


class MyMaxHeapNoNode:
    def __init__(self, nums: List[int]) -> None:
        self.length = len(nums)
        self.nums = nums
        # there is no node

        #         0
        #    1          2
        #  3   4     5     6
        # 7 8 9 10 11 12 13 14

    def sequenced_list(self) -> List[int]:
        return self.nums

    def print_in_sequence(self):
        print(self.sequenced_list())

    def maxHeapifyWholeTrunk(self):
        # STEP 0 : build max heap from some randon array
        # go from bottom to up...
        working_idx = self.length - 1
        while working_idx >= 0:
            self.nums = maxHeapifyList(self.nums, current_root=working_idx)
            working_idx -= 1

    def sortDescending(self) -> List[int]:
        # STEP 1 : find the max element at self.nodes[0]
        # STEP 2 : swap with self.nodes[self.length - 1]
        # STEP 3 : now get rid of the max node at the end, put it in the array,
        # STEP 4 : After the swap, the root's left/right are both max heap still! so, heapify the whole thing
        # STEP 1 ...
        self.maxHeapifyWholeTrunk()
        # destructive!!!!
        sorted: List[int] = []
        while self.length:
            # STEP 4:
            self.nums = maxHeapifyList(self.nums)
            # STEP 1/2:
            self.nums[0], self.nums[self.length - 1] = (
                self.nums[self.length - 1],
                self.nums[0],
            )
            # STEP 3:
            sorted.append(self.nums.pop())
            self.length -= 1

        return sorted


def solution() -> int:
    return 0


if __name__ == "__main__":
    # test_case = []
    # print(solution(test_case))

    #   4
    # 8   9
    print(maxHeapifyList([4, 8, 9]))
    #   9
    # 8   4

    #         0
    #    4          7
    #  3   2     5     6
    print(maxHeapifyList([0, 4, 7, 3, 2, 5, 6]))
    #         7
    #    4          6
    #  3   2     5     0

    #     2
    #  4     5
    # 3 1   0
    print(maxHeapifyList([2, 4, 5, 3, 1, 0]))

    # so maxHeapifyList is correct!!!

    #   9
    # 8   4
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mmh = MyMaxHeapNoNode(nums)

    print("Running the first heapify whole trunk")
    mmh.maxHeapifyWholeTrunk()
    mmh.print_in_sequence()

    # 10
    # 9 6
    # 8 4 5 2
    # 7 3 1 0

    print("time to sort descending")
    nums = mmh.sortDescending()
    print(nums)
