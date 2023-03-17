"""
A game has n levels, connected by m teleporters, and your task is to get from level 1 to level n.
The game has been designed so that there are no directed cycles in the underlying graph.

In how many ways can you complete the game?

Input

The first input line has two integers n and m: the number of levels and teleporters. The levels are numbered 1,2,…,n.

After this, there are m lines describing the teleporters.
Each line has two integers a and b: there is a teleporter from level a to level b.

Output

Print one integer: the number of ways you can complete the game. Since the result may be large, print it modulo 109+7.

Constraints
1≤n≤105
1≤m≤2⋅105
1≤a,b≤n
Example

Input:
4 5
1 2
2 4
1 3
3 4
1 4

Output:
3
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
    class Toposort:
        def __init__(self, n, adj):
            self.graph = collections.defaultdict(list)
            self.backedge = collections.defaultdict(list)
            self.colors = [0] * n
            self.vis = [False] * n
            self.mod = 10 ** 9 + 7
            self.in_degree = [0] * n
            self.n = n

            for v, u in adj:
                self.graph[v].append(u)
                self.backedge[u].append(v)
                self.in_degree[u] += 1

        def dfs_find_all_ways(self):
            def dfs(v):
                self.colors[v] = 1  # handle current vertex
                self.vis[v] = True
                dp[v] = 1 if v == self.n - 1 else 0

                for u in self.graph[v]:
                    if self.colors[u] == 1:
                        print("IMPOSSIBLE")
                        exit(0)
                    else:
                        if not self.vis[u]:
                            dfs(u)
                    # accumulate total number of ways for the vertex V
                    dp[v] = (dp[v] + dp[u]) % self.mod

                self.colors[v] = 0
                return False

            dp = [0] * n
            for v in range(self.n):
                if not self.vis[v]:
                    dfs(v)
            return dp[0]

        def bfs_find_all_ways(self):
            queue = collections.deque()
            for v in range(self.n):
                if self.in_degree[v] == 0:
                    queue.append(v)

            dp = [0] * n
            dp[0] = 1

            while queue:
                v = queue.popleft()

                for u in self.graph[v]:
                    self.in_degree[u] -= 1
                    if self.in_degree[u] == 0:
                        queue.append(u)

                for prev in self.backedge[v]:
                    dp[v] = (dp[v] + dp[prev]) % self.mod

            return dp[n - 1]


    n, m = mp()
    adj = []

    for _ in range(m):
        v, u = mp()
        adj.append((v - 1, u - 1))

    t = Toposort(n, adj)

    print(t.dfs_find_all_ways())
    print(t.bfs_find_all_ways())
