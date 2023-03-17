"""
There are n cities and m roads between them. Your task is to process q queries where you have to determine the length
of the shortest route between two given cities.

Input

The first input line has three integers n, m and q: the number of cities, roads, and queries.

Then, there are m lines describing the roads. Each line has three integers a, b and c:
there is a road between cities a and b whose length is c.
All roads are two-way roads.

Finally, there are q lines describing the queries. Each line has two integers a and b: determine the length of
the shortest route between cities a and b.

Output

Print the length of the shortest route for each query. If there is no route, print −1 instead.

Constraints
1≤n≤500
1≤m≤n2
1≤q≤105
1≤a,b≤n
1≤c≤109
Example

Input:
4 3 5
1 2 5
1 3 9
2 3 3
1 2
2 1
1 3
1 4
3 2

Output:
5
5
8
-1
3
"""

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


def st(): return list(sys.stdin.readline().strip())


if __name__ == '__main__':
    n, m, q = mp()
    graph = []

    # floyd-warshall algo
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][i] = 0

    for _ in range(m):
        v, u, w = mp()
        dp[v][u] = min(dp[v][u], w)
        dp[u][v] = dp[v][u]

    for k in range(1, n + 1):
        for v in range(1, n + 1):
            if k == v: continue
            for u in range(v + 1, n + 1):
                if u == k: continue
                if dp[v][u] > dp[v][k] + dp[k][u]:
                    dp[v][u] = dp[v][k] + dp[k][u]
                    dp[u][v] = dp[v][u]

    for _ in range(q):
        a, b = mp()
        x = dp[a][b]
        print(-1 if x == float('inf') else x)

