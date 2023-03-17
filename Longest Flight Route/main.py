"""
Uolevi has won a contest, and the prize is a free flight trip that can consist of one or more flights through cities.
Of course, Uolevi wants to choose a trip that has as many cities as possible.

Uolevi wants to fly from Syrjälä to Lehmälä so that he visits the maximum number of cities.
You are given the list of possible flights, and you know that there are no directed cycles in the flight network.

Input

The first input line has two integers n and m: the number of cities and flights. The cities are numbered 1,2,…,n.
City 1 is Syrjälä, and city n is Lehmälä.

After this, there are m lines describing the flights. Each line has two integers a and b: there is a flight from city a to city b.
Each flight is a one-way flight.

Output

First print the maximum number of cities on the route. After this, print the cities in the order they will be visited.
You can print any valid solution.

If there are no solutions, print "IMPOSSIBLE".

Constraints
2≤n≤105
1≤m≤2⋅105
1≤a,b≤n
Example

Input:
5 5
1 2
2 5
1 3
3 4
4 5

Output:
4
1 3 4 5
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
            self.adj = adj
            self.in_degree = [0] * n
            self.n = n
            for v, u in adj:
                self.graph[v].append(u)
                self.backedge[u].append(v)
                self.in_degree[u] += 1

        def dfs_longest_path(self):
            def dfs(v):
                colors[v] = 1
                vis[v] = True
                dp[v] = 1 if v == n - 1 else -1e9

                for u in graph[v]:
                    if colors[u] == 1:
                        print("IMPOSSIBLE")
                        exit(0)
                    else:
                        if not vis[u]:
                            prev_vertex[u] = v
                            dfs(u)

                    if dp[u] + 1 > dp[v]:
                        prev_vertex[v] = u
                        dp[v] = dp[u] + 1

                colors[v] = 0
                return False

            dp = [0] * self.n
            vis = [False] * self.n
            colors = [0] * self.n
            prev_vertex = [None] * self.n
            graph = collections.defaultdict(list)

            for v, u in self.adj:
                graph[v].append(u)

            for v in range(self.n):
                if not vis[v]:
                    dfs(v)

            if dp[0] < 0:
                print('IMPOSSIBLE')
            else:
                res = [0]
                v = 0
                while v ^ (n - 1):
                    v = prev_vertex[v]
                    res.append(v)

            print(len(res))
            print(*[x + 1 for x in res])

        def bfs_longest_path(self):
            queue = collections.deque()
            dp = [float('-inf')] * self.n
            prev_vertex = [None] * self.n

            for v in range(self.n):
                if self.in_degree[v] == 0:
                    queue.append(v)

            while queue:
                v = queue.popleft()

                for u in self.graph[v]:
                    self.in_degree[u] -= 1
                    if self.in_degree[u] == 0:
                        queue.append(u)

                max_dist = float('-inf')
                max_prev_vertex = None
                for prev in self.backedge[v]:
                    if dp[prev] + 1 > max_dist:
                        max_dist = dp[prev] + 1
                        max_prev_vertex = prev

                dp[v] = max_dist
                prev_vertex[v] = max_prev_vertex
                if v == 0:
                    dp[v] = 1

            has_path = False
            v = n - 1
            res = []
            while v is not None and dp[v] >= 0:
                res.append(v)
                v = prev_vertex[v]
                if v == 0:
                    has_path = True

            if has_path:
                print(dp[n - 1])
                print(*[x + 1 for x in res][::-1])
            else:
                print('IMPOSSIBLE')


    n, m = mp()
    adj = []

    for _ in range(m):
        v, u = mp()
        adj.append((v - 1, u - 1))

    topo = Toposort(n, adj)
    print('===========DFS==========')
    topo.dfs_longest_path()

    print('===========BFS==========')
    topo.bfs_longest_path()
