"""
Byteland has n cities and m flight connections. Your task is to design a round trip that begins in a city,
goes through one or more other cities, and finally returns to the starting city.

Every intermediate city on the route has to be distinct.

Input

The first input line has two integers n and m: the number of cities and flights. The cities are numbered 1,2,…,n.

Then, there are m lines describing the flights.

Each line has two integers a and b: there is a flight connection from city a to city b.
All connections are one-way flights from a city to another city.

Output

First print an integer k: the number of cities on the route. Then print k cities in the order they will be visited.
You can print any valid solution.

If there are no solutions, print "IMPOSSIBLE".

Constraints
1≤n≤105
1≤m≤2⋅105
1≤a,b≤n
Example

Input:
4 5
1 3
2 1
2 4
3 2
3 4

Output:
4
2 1 3 2
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
    def build_path(v, u):
        path = [v]
        while v ^ u:
            v = p[v]
            path.append(v)
        path.append(path[0])
        print(len(path))
        print(*[x + 1 for x in path[::-1]])
        exit(0)


    def dfs(v):
        colors[v] = 1
        for u in graph[v]:
            if colors[u] == 1:
                build_path(v, u)
                return True
            p[u] = v
            if colors[u] == 0 and dfs(u):
                build_path(v, u)
                return True
        colors[v] = 2
        return False


    n, m = mp()
    graph = collections.defaultdict(list)
    for _ in range(m):
        a, b = mp()
        graph[a - 1].append(b - 1)

    colors = [0] * n
    p = [None] * n

    for v in range(n):
        if colors[v] == 0 and dfs(v):
            break

    print("IMPOSSIBLE")
