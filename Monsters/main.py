"""
Time limit: 1.00 s Memory limit: 512 MB
You and some monsters are in a labyrinth. When taking a step to some direction in the labyrinth, each monster may simultaneously take one as well. Your goal is to reach one of the boundary squares without ever sharing a square with a monster.

Your task is to find out if your goal is possible, and if it is, print a path that you can follow. Your plan has to work in any situation; even if the monsters know your path beforehand.

Input

The first input line has two integers n and m: the height and width of the map.

After this there are n lines of m characters describing the map. Each character is . (floor), # (wall), A (start), or M (monster). There is exactly one A in the input.

Output

First print "YES" if your goal is possible, and "NO" otherwise.

If your goal is possible, also print an example of a valid path (the length of the path and its description using characters D, U, L, and R). You can print any path, as long as its length is at most n⋅m steps.

Constraints
1≤n,m≤1000
Example

Input:
5 8
########
#M..A..#
#.#.M#.#
#M#..#..
#.######

Output:
YES
5
RRDDR
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
    def fill_dist(queue, dist):
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                    if 0 <= x < n and 0 <= y < m:
                        if dist[x][y] > dist[i][j] + 1 and A[x][y] == '.':
                            dist[x][y] = dist[i][j] + 1
                            queue.append((x, y))
        return dist


    def find_path(start, target):
        queue = collections.deque()
        queue.append([start[0], start[1], []])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[start[0]][start[1]] = 0
        while queue:
            i, j, path = queue.popleft()

            if (i, j) == target:
                return path

            for x, y, d in [[i - 1, j, 'U'], [i + 1, j, 'D'], [i, j - 1, 'L'], [i, j + 1, 'R']]:
                if 0 <= x < n and 0 <= y < m:
                    if dist[x][y] > dist[i][j] + 1 and A[x][y] == '.':
                        dist[x][y] = dist[i][j] + 1
                        queue.append([x, y, path + [d]])
        return []


    n, m = mp()
    A = []
    for _ in range(n):
        A.append(st())

    monster_dist = [[float('inf')] * m for _ in range(n)]
    user_dist = [[float('inf')] * m for _ in range(n)]
    user_queue = collections.deque()
    monster_queue = collections.deque()
    borders = []
    user_pos = None
    for i in range(n):
        for j in range(m):
            if A[i][j] == 'A':
                if (i in [0, n - 1] or j in [0, m - 1]):
                    print('YES')
                    print(0)
                    exit()
                user_dist[i][j] = 0
                user_pos = (i, j)
            if A[i][j] == 'M':
                monster_queue.append((i, j))
                monster_dist[i][j] = 0
            if A[i][j] == '.' and (i in [0, n - 1] or j in [0, m - 1]):
                borders.append((i, j))

    dist1 = fill_dist(monster_queue, monster_dist)
    dist2 = fill_dist(collections.deque([user_pos]), user_dist)

    target = None

    for i, j in borders:
        if dist1[i][j] > dist2[i][j]:
            target = (i, j)

    if not target:
        print('NO')
        exit()

    path = find_path(user_pos, target)

    print('YES')
    print(len(path))
    print("".join(path))
