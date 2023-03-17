"""
Given a starting position of a knight on an 8×8 chessboard,
your task is to find a sequence of moves such that it visits every square exactly once.

On each move, the knight may either move two steps horizontally and one step vertically, or one step horizontally and two steps vertically.

Input

The only line has two integers x and y: the knight's starting position.

Output

Print a grid that shows how the knight moves (according to the example). You can print any valid solution.

Constraints
    1≤x,y≤8

Example

Input:
    2 1

Output:
    8 1 10 13 6 3 20 17
    11 14 7 2 19 16 23 4
    26 9 12 15 24 5 18 21
    49 58 25 28 51 22 33 30
    40 27 50 59 32 29 52 35
    57 48 41 44 37 34 31 62
    42 39 46 55 60 63 36 53
    47 56 43 38 45 54 61 64
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


def st(): return sys.stdin.readline().strip()


def mp(): return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    def check(x, y):
        return 0 <= x < 8 and 0 <= y < 8 and visited[x][y] is None


    def deg(x, y):
        d = 0
        for i in range(8):
            d += check(x + di[i], y + dj[i])
        return d


    def dfs(i, j, a):
        visited[i][j] = a + 1

        if a == 63:
            for i in range(8):
                res = []
                for j in range(8):
                    res.append(visited[i][j])
                print(*res)
            exit()

        # evaluate the all possible next pointers and take the most optimal for the next dfs call
        pairs = []

        for k in range(8):
            x, y = i + di[k], j + dj[k]
            if check(x, y):
                pairs.append((x, y))

        pairs.sort(key=lambda x: deg(*x))

        for x, y in pairs:
            dfs(x, y, a + 1)

        visited[i][j] = None


    di = [1, 2, 2, 1, -1, -2, -2, -1]
    dj = [2, 1, -1, -2, -2, -1, 1, 2]
    start_x, start_y = mp()
    start_x, start_y = start_y - 1, start_x - 1
    n = 8
    visited = [[None] * n for _ in range(n)]
    index = (start_x * n) + start_y
    dfs(start_x, start_y, 0)
