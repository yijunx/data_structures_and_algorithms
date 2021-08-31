# problem:
from typing import List


class Node:
    def __init__(self, num) -> None:
        self.val = num
        self.left = None
        self.right = None

    def pretty_print(self):
        print()


def maxHeapify(node: Node) -> Node:
    # assume the left and right node both are max heap already
    # and there wont be any node with right, but left is None
    if node.left is None and node.right is None:
        # leaf
        return node
    elif node.right is None:
        if node.left.val > node.val:
            # swap the value..
            node.left.val, node.val = node.val, node.left.val
            node.left = maxHeapify(node.left)
            return node
        else:
            return node
    else:
        if node.left.val > node.val and node.left.val >= node.right.val:
            # swap left
            node.left.val, node.val = node.val, node.left.val
            node.left = maxHeapify(node.left)
            return node
        elif node.right.val > node.val and node.right.val >= node.left.val:
            # swap right
            node.right.val, node.val = node.val, node.right.val
            node.right = maxHeapify(node.right)
            return node
        else:
            return node


class MyMaxHeap:
    def __init__(self, nums: List[int]) -> None:
        self.length = len(nums)

        #         0
        #    1          2
        #  3   4     5     6
        # 7 8 9 10 11 12 13 14
        self.nodes: List[Node] = []
        for index, num in enumerate(nums):
            node = Node(num)
            self.nodes.append(node)
            if index > 0:
                parent_node = self.nodes[(index - 1) // 2]
                if parent_node.left is None:
                    parent_node.left = node
                else:
                    parent_node.right = node
        self.root = self.nodes[0]

    def sequenced_list(self) -> List[int]:
        nums: List[int] = []
        i = 0
        while i < self.length:
            nums.append(self.nodes[i].val)
            i += 1
        return nums

    def print_in_sequence(self):
        print(self.sequenced_list())

    def maxHeapifyWholeTrunk(self):
        # STEP 0 : build max heap from some randon array
        # go from bottom to up...
        working_idx = self.length - 1
        while working_idx >= 0:
            maxHeapify(self.nodes[working_idx])
            working_idx -= 1

    def sortDescending(self) -> List[int]:
        # STEP 1 : find the max element at self.nodes[0]
        # STEP 2 : swap with self.nodes[self.length - 1]
        # STEP 3 : now get rid of the max node at the end, put it in the array,
        # STEP 4 : After the swap, the root's left/right are both max heap still! so, heapify the whole thing
        # STEP 1 ...

        # destructive!!!!
        nums: List[int] = []
        while self.length:
            # STEP 4:
            self.maxHeapifyWholeTrunk()
            # STEP 1/2:
            self.nodes[0].val, self.nodes[self.length - 1].val = (
                self.nodes[self.length - 1].val,
                self.nodes[0].val,
            )
            # STEP 3:
            nums.append(self.nodes[self.length - 1].val)
            parent_node = self.nodes[(self.length - 1 - 1) // 2]
            if parent_node.right is None:
                parent_node.left = None
            else:
                parent_node.right = None

            self.length -= 1

        return nums


def solution() -> int:
    return 0


if __name__ == "__main__":
    # test_case = []
    # print(solution(test_case))
    node_1 = Node(4)
    node_1.left = Node(8)
    node_1.right = Node(9)

    #   4
    # 8   9
    node_x = maxHeapify(node_1)
    print(node_x.val, node_x.left.val, node_x.right.val)

    #   9
    # 8   4
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mmh = MyMaxHeap(nums)
    print(mmh.root.val)
    print(mmh.root.left.val, mmh.root.right.val)
    print(
        mmh.root.left.left.val,
        mmh.root.left.right.val,
        mmh.root.right.left.val,
        mmh.root.right.right.val,
    )
    mmh.print_in_sequence()

    # print("Running the first heapify whole trunk")
    # mmh.maxHeapifyWholeTrunk()
    # print(mmh.root.val)
    # print(mmh.root.left.val, mmh.root.right.val)
    # print(mmh.root.left.left.val, mmh.root.left.right.val, mmh.root.right.left.val, mmh.root.right.right.val)
    # mmh.print_in_sequence()

    print("time to sort descending")
    nums = mmh.sortDescending()
    print(nums)
    print(mmh.length)
