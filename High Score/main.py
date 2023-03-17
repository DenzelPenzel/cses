"""
You play a game consisting of n rooms and m tunnels. Your initial score is 0, and each tunnel increases your
score by x where x may be both positive or negative. You may go through a tunnel several times.

Your task is to walk from room 1 to room n. What is the maximum score you can get?

Input

The first input line has two integers n and m: the number of rooms and tunnels. The rooms are numbered 1,2,…,n.

Then, there are m lines describing the tunnels. Each line has three integers a, b and x: the tunnel starts at room a,
ends at room b, and it increases your score by x. All tunnels are one-way tunnels.

You can assume that it is possible to get from room 1 to room n.

Output

Print one integer: the maximum score you can get. However, if you can get an arbitrarily large score, print −1.

Constraints
1≤n≤2500
1≤m≤5000
1≤a,b≤n
−109≤x≤109
Example

Input:
4 5
1 2 3
2 4 -1
1 3 -2
3 4 7
1 4 4

Output:
5
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
    def dfs1(v: int):
        vis1[v] = 1
        for u in graph2[v]:
            if not vis1[u]:
                dfs1(u)


    def dfs2(v: int):
        vis2[v] = 1
        for u, _ in graph1[v]:
            if not vis2[u]:
                dfs2(u)

    n, m = mp()
    graph1 = collections.defaultdict(list)
    graph2 = collections.defaultdict(list)
    start_v = 0
    vis1 = [0] * n
    vis2 = [0] * n

    for _ in range(m):
        v, u, w = mp()
        graph1[v - 1].append([u - 1, w])
        graph2[u - 1].append(v - 1)

    dp = [float('-inf')] * n
    dp[start_v] = 0

    dfs1(n - 1)
    dfs2(0)

    # why use 2*n iterations?
    for i in range(2 * n):
        ch = False
        for v in range(n):
            for u, w in graph1[v]:
                if dp[v] != float('-inf') and dp[v] + w > dp[u]:
                    if vis1[u] and vis2[u]:
                        ch = True
                    dp[u] = dp[v] + w
        # return -1 only when it is possible to reach to last node from the cycle
        if i >= n - 1 and ch:
            print(-1)
            exit()

    print(dp[n - 1])
