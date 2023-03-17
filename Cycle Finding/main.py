"""
You are given a directed graph, and your task is to find out if it contains a negative cycle,
and also give an example of such a cycle.

Input

The first input line has two integers n and m: the number of nodes and edges. The nodes are numbered 1,2,…,n.

After this, the input has m lines describing the edges. Each line has three integers a, b, and c:
there is an edge from node a to node b whose length is c.

Output

If the graph contains a negative cycle, print first "YES", and then the nodes in the cycle in their correct order.
If there are several negative cycles, you can print any of them. If there are no negative cycles, print "NO".

Constraints
1≤n≤2500
1≤m≤5000
1≤a,b≤n
−109≤c≤109
Example

Input:
4 5
1 2 1
2 4 1
3 1 1
4 1 -3
4 3 -2

Output:
YES
1 2 4 1
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
    graph = collections.defaultdict(list)

    for _ in range(m):
        v, u, w = mp()
        graph[v - 1].append((u - 1, w))

    dp = [0] * n
    prev = [None] * n

    for i in range(5 * n):
        for v in range(n):
            for u, w in graph[v]:
                if dp[u] > dp[v] + w:
                    dp[u] = dp[v] + w
                    prev[u] = v
                    """
                        if there is no negative in the cycles in graph 
                        then after n−1 rounds the distances can no longer change
                        because any shortest path contains at most n − 1 edges
                        
                        if after n-1 rounds cond (dp[v] + w < dp[u]) is valid 
                        then there is negative cycle
                    """
                    if i == n - 1:  # find the negative cycle
                        print('YES')
                        ans = []
                        vv = v
                        ans.append(vv + 1)
                        vv = prev[vv]

                        while v ^ vv:
                            ans.append(vv + 1)
                            vv = prev[vv]

                        ans.append(vv + 1)  # add current vertex as a start point of cycle

                        # print cycle
                        print(*ans[::-1])
                        exit(0)

    print('NO')
