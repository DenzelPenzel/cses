"""
Byteland has n cities and m roads between them. Your task is to design a round trip that begins in a city, goes through
two or more other cities, and finally returns to the starting city.
Every intermediate city on the route has to be distinct.

Input

The first input line has two integers n and m: the number of cities and roads. The cities are numbered 1,2,…,n.

Then, there are m lines describing the roads. Each line has two integers a and b: there is a road between those cities.

Every road is between two different cities, and there is at most one road between any two cities.

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
5 6
1 3
1 2
5 3
1 5
2 4
4 5

Output:
4
3 5 1 3
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
    def DFS(v, parent, path):
        global has_path, res

        if has_path: return

        if v in seen:
            if len(path) > 2:
                has_path = True
                cur = [v]
                while path and path[-1] != v:
                    cur.append(path.pop())
                cur.append(path.pop())
                res = cur
            return

        seen.add(v)
        path.append(v)

        for u in graph[v]:
            if u == parent: continue
            DFS(u, v, path)
        # backtracking
        if path:
            path.pop()

    n, m = mp()
    graph = collections.defaultdict(list)
    for _ in range(m):
        a, b = mp()
        graph[a].append(b)
        graph[b].append(a)

    seen = set()
    res = []
    has_path = False
    for k in range(1, n + 1):
        if k not in seen:
            DFS(k, None, [])
            if has_path:
                break

    if not res:
        print('IMPOSSIBLE')
    else:
        print(len(res))
        print(*res)
