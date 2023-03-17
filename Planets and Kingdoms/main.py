"""
A game has n planets, connected by m teleporters.
Two planets a and b belong to the same kingdom exactly when there is a route both from a to b and from b to a.
Your task is to determine for each planet its kingdom.

Input
The first input line has two integers n and m: the number of planets and teleporters.
The planets are numbered 1,2,…,n.

After this, there are m lines describing the teleporters.
Each line has two integers a and b: you can travel from planet a to planet b through a teleporter.

Output

First print an integer k: the number of kingdoms.
After this, print for each planet a kingdom label between 1 and k.
You can print any valid solution.

Constraints
1≤n≤105
1≤m≤2⋅105
1≤a,b≤n

Example

Input:
5 6
1 2
2 3
3 1
3 4
4 5
5 4

Output:
2
1 1 1 2 2
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
    def dfs1(v: int):
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                dfs1(u)
        stack.append(v)


    def dfs2(v: int):
        component[v] = idx
        components[idx].append(v)
        visited[v] = True
        for u in rev_graph[v]:
            if not visited[u]:
                dfs2(u)


    n, m = mp()
    graph = collections.defaultdict(list)
    rev_graph = collections.defaultdict(list)
    stack = []
    visited = [False] * n
    component = [0] * n
    components = collections.defaultdict(list)
    idx = 0

    for _ in range(m):
        v, u = mp()
        graph[v - 1].append(u - 1)
        rev_graph[u - 1].append(v - 1)

    for v in range(n):
        if not visited[v]:
            dfs1(v)

    visited = [False] * n

    while stack:
        v = stack.pop()
        if not visited[v]:
            dfs2(v)
            idx += 1

    print(idx)
    res = [component[v] + 1 for v in range(n)]
    print(*res)
