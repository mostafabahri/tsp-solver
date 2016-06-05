'''
Travelling Sales Person problem
Bround and bound algorithm

gitHub@MostafaBahri
gitLab@Mostafa_c6
'''
from utility import Node, PriorityQueue


def travel(adj_mat, src=0):
    optimal_tour = []
    n = len(adj_mat)
    if not n:
        raise ValueError("Invalid adj Matrix")
    u = Node()
    PQ = PriorityQueue()
    optimal_length = 0
    v = Node(level=0, path=[0])
    min_length = float('inf')  # infinity
    v.bound = bound(adj_mat, v)
    PQ.put(v)
    while not PQ.empty():
        v = PQ.get()
        if v.bound < min_length:
            u.level = v.level + 1
            for i in filter(lambda x: x not in v.path, range(1, n)):
                u.path = v.path[:]
                u.path.append(i)
                if u.level == n - 2:
                    l = set(range(1, n)) - set(u.path)
                    u.path.append(list(l)[0])
                    # putting the first vertex at last
                    u.path.append(0)

                    _len = length(adj_mat, u)
                    if _len < min_length:
                        min_length = _len
                        optimal_length = _len
                        optimal_tour = u.path[:]

                else:
                    u.bound = bound(adj_mat, u)
                    if u.bound < min_length:
                        PQ.put(u)
                # make a new node at each iteration! python it is!!
                u = Node(level=u.level)

    # shifting to proper source(start of path)
    optimal_tour_src = optimal_tour
    if src is not 1:
        optimal_tour_src = optimal_tour[:-1]
        y = optimal_tour_src.index(src)
        optimal_tour_src = optimal_tour_src[y:] + optimal_tour_src[:y]
        optimal_tour_src.append(optimal_tour_src[0])

    return optimal_tour_src, optimal_length


def length(adj_mat, node):
    tour = node.path
    # returns the sum of two consecutive elements of tour in adj[i][j]
    return sum([adj_mat[tour[i]][tour[i + 1]] for i in xrange(len(tour) - 1)])


def bound(adj_mat, node):
    path = node.path
    _bound = 0

    n = len(adj_mat)
    determined, last = path[:-1], path[-1]
    # remain is index based
    remain = filter(lambda x: x not in path, range(n))

    # for the edges that are certain
    for i in xrange(len(path) - 1):
        _bound += adj_mat[path[i]][path[i + 1]]

    # for the last item
    _bound += min([adj_mat[last][i] for i in remain])

    p = [path[0]] + remain
    # for the undetermined nodes
    for r in remain:
        _bound += min([adj_mat[r][i] for i in filter(lambda x: x != r, p)])
    return _bound



if __name__ == '__main__':

	matrix = [
	    [0, 14, 4, 10, 20],
	    [14, 0, 7, 8, 7],
	    [4, 5, 0, 7, 16],
	    [11, 7, 9, 0, 2],
	    [18, 7, 17, 4, 0]
	]

	print travel(matrix)
