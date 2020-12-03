from random import sample
from time import time
from P2 import MinHeap
import heapq


class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError  # TODO

    def get(self):
        raise NotImplementedError  # TODO

    def peek(self):
        raise NotImplementedError  # TODO


class NaivePriorityQueue(PriorityQueue):
    def put(self, val):
        if len(self.elements) >= self.max_size:
            raise IndexError('Max Size Has Reached')
        self.elements.append(val)

    def get(self):
        if len(self.elements) == 0:
            raise IndexError('Empty Priority Queue')

        val = self.peek()
        self.elements.remove(val)
        return val

    def peek(self):
        if len(self.elements) == 0:
            raise IndexError('Empty Priority Queue')
        return min(self.elements)


class HeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        self.max_size = max_size
        self.elements = MinHeap([])

    def put(self, val):
        if len(self.elements) >= self.max_size:
            raise IndexError('Max Size has reached')
        self.elements.heappush(val)

    def get(self):
        if len(self) == 0:
            raise IndexError('Empty Priority Queue')
        return self.elements.heappop()

    def peek(self):
        if len(self) == 0:
            raise IndexError('Empty Priority Queue')
        return self.elements.elements[0]


class PythonHeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        self.max_size = max_size
        self.elements = []
        heapq.heapify(self.elements)

    def put(self, val):
        if len(self.elements) >= self.max_size:
            raise IndexError('Max Size has reached')
        heapq.heappush(self.elements, val)

    def get(self):
        if len(self) == 0:
            raise IndexError('Empty Priority Queue')
        return heapq.heappop(self.elements)

    def peek(self):
        if len(self) == 0:
            raise IndexError('Empty Priority Queue')
        return self.elements[0]


def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists):
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i))

    return merged


def generatelists(n, length=20, dictionary_path='words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end = time()
            timeaccum += end - start
        elapsed.append(timeaccum / n_average)
    return elapsed


if __name__ == "__main__":
    print("====part A====")
    testList = [5, 1, 4, 2, 6, 7]
    print("Naive Implementation")
    q = NaivePriorityQueue(10)
    for t in testList:
        q.put(t)
    print(q.peek())
    while q:
        print(q.get())
    try:
        q.get()
    except Exception as e:
        print(e)
    print()

    print("====part B====")
    testList = [4, 2, 3, 0, 9]
    print("Self-Implement Heap")
    q = HeapPriorityQueue(10)
    for t in testList:
        q.put(t)
    print(q.peek())
    while q:
        print(q.get())
    try:
        q.get()
    except Exception as e:
        print(e)

    print("Python Heap")
    testList = [2, 6, 3, 4, 5, 9, 0]
    q = PythonHeapPriorityQueue(8)
    for t in testList:
        q.put(t)
    print(q.peek())
    while q:
        print(q.get())
    try:
        q.get()
    except Exception as e:
        print(e)
