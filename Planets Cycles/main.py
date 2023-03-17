"""
You are playing a game consisting of n planets.
Each planet has a teleporter to another planet (or the planet itself).

You start on a planet and then travel through teleporters until you reach a planet that you have already visited before.

Your task is to calculate for each planet the number of teleportations there would be if you started on that planet.

Input:
The first input line has an integer n: the number of planets. The planets are numbered 1,2,…,n.
The second line has n integers t1,t2,…,tn: for each planet, the destination of the teleporter. It is possible that ti=i.

Output:
Print n integers according to the problem statement.

Constraints
1≤n≤2⋅105
1≤ti≤n

Example

Input:
5
2 4 3 1 4

Output:
3 3 1 3 4
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
    def dfs(v: int) -> None:
        global steps
        path.append(v)
        if visited[v]:
            # add pathlength of the repeat vertex to current step count
            steps += pathlength[v]
            return
        visited[v] = True
        steps += 1
        dfs(A[v])


    n = int(input().strip())
    A = [None] * n
    for i, x in enumerate(mp()):
        A[i] = x - 1

    visited = [False] * n
    pathlength = [0] * n
    path = collections.deque()
    steps = 0

    for v in range(n):
        if not visited[v]:
            steps = 0
            dfs(v)
            decrement = 1
            while path:
                if path[0] == path[-1]:
                    decrement = 0
                pathlength[path[0]] = steps
                steps -= decrement
                path.popleft()

    print(*pathlength)
