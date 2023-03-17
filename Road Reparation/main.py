"""
There are n cities and m roads between them.
Unfortunately, the condition of the roads is so poor that they cannot be used.
Your task is to repair some of the roads so that there will be a decent route between any two cities.

For each road, you know its reparation cost, and you should find a solution where the total cost is as small as possible.

Input

The first input line has two integers n and m: the number of cities and roads. The cities are numbered 1,2,…,n.

Then, there are m lines describing the roads.
Each line has three integers a, b and c: there is a road between cities a and b, and its reparation cost is c.
All roads are two-way roads.

Every road is between two different cities, and there is at most one road between two cities.

Output

Print one integer: the minimum total reparation cost. However, if there are no solutions, print "IMPOSSIBLE".

Constraints
1≤n≤105

1≤m≤2⋅105

1≤a,b≤n

1≤c≤109

Example

Input:
5 6
1 2 3
2 3 5
2 4 2
3 4 8
5 1 7
5 4 4

Output:
14
"""

import collections
import os
import sys
from typing import List


def read_file(fname: str):
    with open(fname, mode='r') as f:
        content = f.readlines()
        context = [list(map(int, x.strip().split(' '))) for x in content]
    return context


if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')


def mp(): return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    class Kruskal:
        def __init__(self, n: int, graph: List[List[int]]):
            self.graph = graph
            self.n = n
            self.parent = [i for i in range(n + 1)]
            self.graph.sort(key=lambda x: x[2])  # sort by weight

        def find(self, x: int):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x: int, y: int):
            xr, yr = self.find(x), self.find(y)
            if xr != yr:
                self.parent[yr] = xr
                return True

        def get_count_components(self) -> int:
            return sum([1 for i in range(self.n) if self.parent[i] == i])

        def weight(self) -> int:
            res = 0
            for v, u, w in self.graph:
                if self.union(v, u):
                    res += w
            return 'IMPOSSIBLE' if self.get_count_components() > 1 else res


    n, m = mp()
    graph = []
    adj = collections.defaultdict(list)
    for _ in range(m):
        v, u, w = mp()
        graph.append((v - 1, u - 1, w))

    mst = Kruskal(n, graph)
    print(mst.weight())