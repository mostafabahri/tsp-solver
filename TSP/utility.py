'''
Node class 
and sample Priority Queue 
'''
from Queue import PriorityQueue

pq = PriorityQueue()


class Node(object):
    def __init__(self, level=None, path=None, bound=None):
        self.level = level
        self.path = path
        self.bound = bound

    def __cmp__(self, other):
        return cmp(self.bound, other.bound)

    def __str__(self):
        return str(tuple([self.level, self.path, self.bound]))


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.put(Node(2, [1, 2, 3], 6))
    pq.put(Node(4, [1, 3, 2], 1))
    pq.put(Node(1, [1, 2], 7))
    while not pq.empty():
        print pq.get()

    pq.put(Node(3, [1, 2, 5], 12))

