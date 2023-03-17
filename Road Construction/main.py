"""
There are n cities and initially no roads between them.
However, every day a new road will be constructed, and there will be a total of m  roads.

A component is a group of cities where there is a route between any two cities using the roads.
After each day, your task is to find the number of components and the size of the largest component.

Input

The first input line has two integers n and m: the number of cities and roads. The cities are numbered 1,2,…,n.

Then, there are m lines describing the new roads.
Each line has two integers a and b: a new road is constructed between cities a and b.

You may assume that every road will be constructed between two different cities.

Output

Print m
 lines: the required information after each day.

Constraints
1≤n≤105

1≤m≤2⋅105

1≤a,b≤n

Example

Input:
5 3
1 2
1 3
4 5

Output:
4 2
3 3
2 3
"""

import collections
import os
import sys


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
    class UnionFind:
        def __init__(self, n: int):
            self.n = n
            self.parent = [i for i in range(n + 1)]
            self.freq = [1] * self.n

        def find(self, x: int):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x: int, y: int):
            xr, yr = self.find(x), self.find(y)
            if xr != yr:
                self.parent[xr] = yr
                self.freq[yr] += self.freq[xr]
                return True

        def get_largest_group(self) -> int:
            return max(self.freq)

    n, m = mp()
    uf = UnionFind(n)
    adj = collections.defaultdict(list)
    graph = []
    count = n
    largest_group = 1
    for _ in range(m):
        v, u = mp()
        if uf.union(v - 1, u - 1):
            count -= 1
            largest_group = uf.get_largest_group()
        print(count, largest_group)
