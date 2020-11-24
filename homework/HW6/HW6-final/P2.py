from math import floor
from typing import List


class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            #buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> str:
        return self.size

    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError

    def heapify(self, idx: int) -> None:
        if idx >= self.size:
            return
        l, r = self.left(idx), self.right(idx)
        extreme_val = idx
        if l < self.size and self.compare(self.elements[l], self.elements[idx]):
            extreme_val = l
        if r < self.size and self.compare(self.elements[r], self.elements[extreme_val]):
            extreme_val = r
        if extreme_val != idx:
            self.swap(idx, extreme_val)
            self.heapify(extreme_val)

    def build_heap(self) -> None:
        for i in range(self.size//2, -1, -1):
            self.heapify(i)

    def heappush(self, key: int) -> None:
        def _heapify_up(idx):
            curr_val = self.elements[idx]
            parentIndex = self.parent(idx)
            while idx > 0 and self.compare(curr_val, self.elements[parentIndex]):
                self.elements[idx] = self.elements[parentIndex]
                idx = parentIndex
                parentIndex = self.parent(parentIndex)
            self.elements[idx] = curr_val

        self.elements.append(key)
        self.size += 1
        _heapify_up(self.size-1)

    def heappop(self) -> int:
        if self.size == 0:
            raise IndexError()
        removed_element = self.elements[0]
        self.elements[0] = self.elements[-1]
        self.elements.pop()
        self.size -= 1
        self.heapify(0)
        return removed_element


class MinHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        return a < b


class MaxHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        return a > b


if __name__ == "__main__":
    print("====part A====")
    h = MinHeap([-1, 0, 0, 15, 23, 1, 2, 3])  # The heap tree will be built during initialization
    print(h)

    print("====part B====")
    h = MinHeap([])
    testList = [-1, 0, 0, 15, 23, 1, 2, 3]
    for i in testList:
        h.heappush(i)
    print(h)
    while len(h) > 0:
        print(h.heappop())
    try:
        h.heappop()
    except Exception as e:
        print(e)
    print()

    print("====part C====")
    mn = MinHeap([1, 2, 3, 4, 5])
    mx = MaxHeap([1, 2, 3, 4, 5])

    print(mn)
    print(mx)

    while len(mn) > 0:
        print(mn.heappop())
    while len(mx) > 0:
        print(mx.heappop())
