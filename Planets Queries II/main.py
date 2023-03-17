"""
You are playing a game consisting of n planets. Each planet has a teleporter to another planet (or the planet itself).

You have to process q queries of the form: You are now on planet a and want to reach planet b.
What is the minimum number of teleportations?

Input

The first input line contains two integers n and q : the number of planets and queries.
The planets are numbered 1,2,…,n.

The second line contains n integers t1,t2,…,tn: for each planet, the destination of the teleporter.

Finally, there are q lines describing the queries.
Each line has two integers a and b: you are now on planet a and want to reach planet b.

Output

For each query, print the minimum number of teleportations.
If it is not possible to reach the destination, print −1.

Constraints
1≤n,q≤2⋅105

1≤a,b≤n

Example

Input:
5 3
2 3 2 3 2
1 2
1 3
1 4

Output:
1
2
-1
"""

import collections
import os
import sys
from typing import List, DefaultDict


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
    from collections import defaultdict


class Tarjan:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.n = n
        self.timestamp = 0
        self.low = [0] * (n + 1)
        self.disc = [0] * (n + 1)
        self.on_stack = [False] * (n + 1)
        self.stack = []
        self.scc_count = 0
        self.scc = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def tarjan(self, u):
        self.disc[u] = self.low[u] = self.timestamp = self.timestamp + 1
        self.stack.append(u)
        self.on_stack[u] = True

        for v in self.graph[u]:
            if self.disc[v] == 0:
                self.tarjan(v)
                self.low[u] = min(self.low[u], self.low[v])
            elif self.on_stack[v]:
                self.low[u] = min(self.low[u], self.disc[v])

        if self.low[u] == self.disc[u]:
            self.scc_count = self.scc_count + 1
            curr_scc = []
            while True:
                v = self.stack.pop()
                self.on_stack[v] = False
                curr_scc.append(v)
                if u == v:
                    break
            self.scc.append(curr_scc)

    def get_scc(self):
        for i in range(1, self.n + 1):
            if self.disc[i] == 0:
                self.tarjan(i)
        return self.scc


def calculate_dist_for_scc(n, q, teleporters, queries):
    tarjan = Tarjan(n)
    for v in range(n):
        u = teleporters[v]
        tarjan.add_edge(v, u - 1)

    scc = tarjan.get_scc()

    adj = collections.defaultdict(list)
    for v, component in enumerate(scc):
        for node in component:
            adj[v].append(node)

    visited = set()
    queue = collections.deque()
    dist = {}

    for s_v in range(n):
        if s_v not in visited:
            queue.append((s_v, 0))
            visited.add(s_v)
            while queue:
                v, d = queue.popleft()
                for u in adj[v]:
                    if u not in visited:
                        visited.add(u)
                        queue.append((u, d + 1))
                        dist[(v, u)] = d + 1

    result = [-1] * n
    for i, query in enumerate(queries):
        a, b = query
        a, b = a - 1, b - 1
        if (a, b) in dist:
            result[i] = dist[(a, b)]
    return result


if __name__ == '__main__':
    n, q = mp()
    teleporters = list(mp())
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    result = calculate_dist_for_scc(n, q, teleporters, queries)
    print(*result)
