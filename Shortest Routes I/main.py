"""


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


def st(): return list(sys.stdin.readline().strip())


if __name__ == '__main__':
    n, m = mp()
    graph = []
    for _ in range(m):
        v, u, w = mp()
        graph.append([v - 1, u - 1, w])

    # bellman-ford
    INF = float('inf')
    dp = [[INF] * n for _ in range(n)]
    dp[0][0] = 0
    res = [0] * n

    for k in range(n - 1):
        dp[k + 1] = dp[k]
        for v, u, w in graph:
            dp[k + 1][u] = min(dp[k + 1][u], dp[k][v] + w)

    for k in range(n):
        res[k] = dp[0][k]

    print(*res)