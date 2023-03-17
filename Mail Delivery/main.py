"""
Your task is to deliver mail to the inhabitants of a city.
For this reason, you want to find a route whose starting and ending point are the post office,
and that goes through every street exactly once.

Input

The first input line has two integers n and m: the number of crossings and streets.
The crossings are numbered 1,2,…,n, and the post office is located at crossing 1.

After that, there are m lines describing the streets.
Each line has two integers a and b: there is a street between crossings a and b. All streets are two-way streets.

Every street is between two different crossings, and there is at most one street between two crossings.

Output

Print all the crossings on the route in the order you will visit them. You can print any valid solution.

If there are no solutions, print "IMPOSSIBLE".

Constraints
2≤n≤105
1≤m≤2.105
1≤a,b≤n

Example

Input:
6 8
1 2
1 3
2 3
2 4
2 6
3 5
3 6
4 5

Output:
1 2 6 3 2 4 5 3 1
"""

import collections
import os
import sys
from typing import List, DefaultDict


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
    n, m = mp()
    graph = collections.defaultdict(list)
    for _ in range(m):
        v, u = mp()
        graph[v].append(u)
        graph[u].append(v)

    # Count the number of vertices with odd degree
    odd_degree_vertices = [v for v in graph if len(graph[v]) % 2 == 1]

    if len(odd_degree_vertices) not in (0, 2):
        print('IMPOSSIBLE')
        exit()

    # Determine the starting vertex
    start_vertex = 1
    if len(odd_degree_vertices) == 2:
        start_vertex = odd_degree_vertices[0]

    # Find the Eulerian path
    path = []
    stack = [start_vertex]
    while stack:
        u = stack[-1]
        if graph[u]:
            v = graph[u].pop()
            graph[v].remove(u)
            stack.append(v)
        else:
            path.append(u)
            stack.pop()

    if len(path) != m + 1 or path[0] != start_vertex:
        print("IMPOSSIBLE")
        exit()

    print(*path)
