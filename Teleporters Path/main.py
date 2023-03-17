"""
A game has n levels and m teleportes between them.
You win the game if you move from level 1 to level n using every teleporter exactly once.

Can you win the game, and what is a possible way to do it?

Input

The first input line has two integers n and m: the number of levels and teleporters. The levels are numbered 1,2,…,n.

Then, there are m lines describing the teleporters.
Each line has two integers a and b: there is a teleporter from level a to level b.

You can assume that each pair (a,b) in the input is distinct.

Output

Print m+1 integers: the sequence in which you visit the levels during the game.
You can print any valid solution.

If there are no solutions, print "IMPOSSIBLE".

Constraints
    2≤n≤105
    1≤m≤2⋅105
    1≤a,b≤n

Example
    Input:
    5 6
    1 2
    1 3
    2 4
    2 5
    3 1
    4 2

    Output:
    1 3 1 2 4 2 5
"""

import collections
import os
import sys

sys.setrecursionlimit(10 ** 6)


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
    edges = []
    in_degrees = [0] * n
    out_degrees = [0] * n

    if n > m:
        print("IMPOSSIBLE")
        exit()

    for i in range(m):
        u, v = mp()
        edges.append((u - 1, v - 1))
        out_degrees[u - 1] += 1
        in_degrees[v - 1] += 1

    start_node = None
    end_node = None

    for i in range(n):
        if in_degrees[i] == out_degrees[i] + 1:
            if end_node is not None:
                print("IMPOSSIBLE")
                exit()
            end_node = i
        elif out_degrees[i] == in_degrees[i] + 1:
            if start_node is not None:
                print("IMPOSSIBLE")
                exit()
            start_node = i
        elif in_degrees[i] != out_degrees[i]:
            print("IMPOSSIBLE")
            exit()

    if start_node is None or end_node is None:
        print("IMPOSSIBLE")
        exit()

    graph = collections.defaultdict(list)

    for u, v in edges:
        graph[u].append(v)

    stack = [start_node]
    path = []

    while stack:
        u = stack[-1]
        if graph[u]:
            v = graph[u].pop()
            stack.append(v)
        else:
            path.append(stack.pop())

    path.reverse()

    res = ' '.join([str(x + 1) for x in path])

    print(res)
