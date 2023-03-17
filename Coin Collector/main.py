"""
A game has n rooms and m tunnels between them.
Each room has a certain number of coins.
What is the maximum number of coins you can collect while moving through the tunnels
when you can freely choose your starting and ending room?

Input

The first input line has two integers n and m: the number of rooms and tunnels. The rooms are numbered 1,2,…,n.

Then, there are n integers k1,k2,…,kn: the number of coins in each room.

Finally, there are m lines describing the tunnels.
Each line has two integers a and b: there is a tunnel from room a to room b. Each tunnel is a one-way tunnel.

Output
Print one integer: the maximum number of coins you can collect.

Constraints
1≤n≤105
1≤m≤2⋅105
1≤ki≤109
1≤a,b≤n

Example

Input:
4 4
4 5 2 7
1 2
2 1
1 3
2 4

Output:
16
"""

import collections
import os
import sys
from typing import DefaultDict, List, Tuple


def read_file(fname: str):
    with open(fname, mode='r') as f:
        content = f.readlines()
        context = [list(map(int, x.strip().split(' '))) for x in content]
    return context


if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')


def st(): return sys.stdin.readline().strip()


def mp(): return map(int, sys.stdin.readline().split())


class SCC:
    def __init__(self, N: int) -> None:
        self.N = N
        self.adj = [[] for _ in range(self.N)]
        self.radj = [[] for _ in range(self.N)]
        self.stack = []
        self.comps = []  # store list of component vertexes
        self.vertex_to_comp = [-1] * self.N
        self.vis = [False] * self.N

    def build_graph(self, x: int, y: int) -> None:
        self.adj[x].append(y)
        self.radj[y].append(x)

    def dfs1(self, x: int) -> None:
        self.vis[x] = True
        for y in self.adj[x]:
            if not self.vis[y]:
                self.dfs1(y)
        self.stack.append(x)

    def dfs2(self, v: int, root: int) -> None:
        self.vertex_to_comp[v] = root
        for u in self.radj[v]:
            if self.vertex_to_comp[u] == -1:
                self.dfs2(u, root)

    def get_scc(self, _N: int) -> None:
        for i in range(1, _N + 1):
            if not self.vis[i]:
                self.dfs1(i)
        # fill vertex_to_comp mapping
        for x in self.stack[::-1]:
            if self.vertex_to_comp[x] == -1:
                self.dfs2(x, x)
                self.comps.append(x)


def DP(v: int, dp: List[int], group: List[int], rgraph: List[List[int]]) -> int:
    if dp[v]:
        return dp[v]

    dp[v] = group[v]
    for u in rgraph[v]:
        dp[v] = max(dp[v], DP(u, dp, group, rgraph) + group[v])

    return dp[v]


def solve(n: int, coins: List[int], edges: List[Tuple[int, int]]) -> int:
    scc = SCC(n + 1)

    for a, b in edges:
        scc.build_graph(a, b)

    scc.get_scc(n)

    print(scc.comps, scc.vertex_to_comp)

    dp = [0] * (n + 1)
    group = [0] * (n + 1)
    rgraph = [[] for _ in range(n + 1)]

    # calculate the sum for the each group
    for v in range(1, n + 1):
        group_id = scc.vertex_to_comp[v]
        group[group_id] += coins[v]

    # create reverse edges for SCC
    for v in range(1, n + 1):
        for u in scc.adj[v]:
            # skip if edge (v -> u) already in the same scc
            if scc.vertex_to_comp[v] == scc.vertex_to_comp[u]:
                continue
            # connect different scc
            rgraph[scc.vertex_to_comp[u]].append(scc.vertex_to_comp[v])

    ans = 0
    # find dp value for each SCC
    for v in scc.comps:
        ans = max(ans, DP(v, dp, group, rgraph))

    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    coins = [0] + list(map(int, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    ans = solve(n, coins, edges)

    print(ans)
