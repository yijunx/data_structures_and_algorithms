# problem:
# make a list of numbers into a bst
# then implement the insertion and deletion
# and output a sorted list..

from typing import List

class AugmentedNode():
    def __init__(self, val) -> None:
        self.val = val
        self.passing_by = 1
        # some pointers..
        self.left = None
        self.right = None
        self.parent = None


def put_into_a_tree(nums: List[int]) -> AugmentedNode:
    root = None
    while len(nums):
        a_node = AugmentedNode(nums.pop())
        if root is None:
            root = a_node
        else:
            if a_node.val 
        



    return


if __name__ == "__main__":
    test_case = []
    print(solution(test_case))