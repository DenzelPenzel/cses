"""
There are n cities and m flight connections.
Your task is to check if you can travel from any city to any other city using the available flights.

Input

The first input line has two integers n and m: the number of cities and flights. The cities are numbered 1,2,…,n.

After this, there are m lines describing the flights.
Each line has two integers a and b: there is a flight from city a to city b. All flights are one-way flights.

Output

Print "YES" if all routes are possible, and "NO" otherwise.
In the latter case also print two cities a and b such that you cannot travel from city ato city b.
If there are several possible solutions, you can print any of them.

Constraints
1≤n≤105

1≤m≤2⋅105

1≤a,b≤n

Example

Input:
4 5
1 2
2 3
3 1
1 4
3 4

Output:
NO
4 2
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

"""
    The theorem used here is that if one vertex can both reach and be reached by all others, 
    then every vertex in this graph can reach all others
    
    Let's say can[v][u] - is true if you can go from vertex v  to vertex u through a series of edges.
    
    Then if can[1][x] == TRUE for 1 <= x <= n in both `adj` and `rev_adj` the answer is "YES"
"""
if __name__ == '__main__':

    def dfs1(v):
        if v in vis1:
            return
        vis1.add(v)
        for u in adj[v]:
            if v == u: continue
            dfs1(u)


    def dfs2(v):
        if v in vis2:
            return
        vis2.add(v)
        for u in rev_adj[v]:
            if v == u: continue
            dfs2(u)


    n, m = mp()
    adj = collections.defaultdict(list)
    rev_adj = collections.defaultdict(list)
    for _ in range(m):
        v, u = mp()
        adj[v - 1].append(u - 1)
        rev_adj[u - 1].append(v - 1)

    vis1 = set()
    vis2 = set()
    dfs1(0)
    dfs2(0)

    for v in range(1, n):
        if v not in vis1:
            print('NO')
            print(*[1, v + 1])
            exit(0)

        if v not in vis2:
            print('NO')
            print(*[v + 1, 1])
            exit(0)

    print('YES')
