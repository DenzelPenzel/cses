"""
You have to complete n courses. There are m requirements of the form "course a has to be completed before course b".
Your task is to find an order in which you can complete the courses.

Input

The first input line has two integers n and m: the number of courses and requirements. The courses are numbered 1,2,…,n.

After this, there are m lines describing the requirements. Each line has two integers a and b:
course a has to be completed before course b.

Output

Print an order in which you can complete the courses. You can print any valid order that includes all the courses.

If there are no solutions, print "IMPOSSIBLE".

Constraints
1≤n≤105
1≤m≤2⋅105
1≤a,b≤n
Example

Input:
5 3
1 2
3 1
4 5

Output:
3 4 1 5 2
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
    def dfs(v):
        colors[v] = 1
        for u in graph[v]:
            if colors[u] == 1:
                return True
            if colors[u] == 0 and dfs(u):
                return True
        res.append(v + 1)
        colors[v] = 2
        return False


    res = []
    n, m = mp()
    graph = collections.defaultdict(list)

    for _ in range(m):
        a, b = mp()
        graph[a - 1].append(b - 1)
    colors = [0] * n
    for v in range(n):
        if colors[v] == 0 and dfs(v):
            print("IMPOSSIBLE")
            exit(0)
    print(*res[::-1])
