"""
You are given a map of a labyrinth, and your task is to find a path from start to end. You can walk left, right, up and down.

Input

The first input line has two integers n and m: the height and width of the map.

Then there are n lines of m characters describing the labyrinth.
Each character is . (floor), # (wall), A (start), or B (end).

There is exactly one A and one B in the input.

Output

First print "YES", if there is a path, and "NO" otherwise.

If there is a path, print the length of the shortest such path and
its description as a string consisting of characters L (left), R (right), U (up), and D (down).

You can print any valid solution.

Constraints
1≤n,m≤1000
Example

Input:
5 8
########
#.A#...#
#.##.#B#
#......#
########

Output:
YES
9
LDDRRRRRU
"""
import collections
from typing import List

if __name__ == '__main__':
    def find(A: List[List[str]]) -> int:
        target = None
        queue = collections.deque()
        for i in range(n):
            for j in range(m):
                if A[i][j] == 'A':
                    queue.append((i, j, []))
                if A[i][j] == 'B':
                    target = (i, j)
        if A[queue[0][0]][queue[0][1]] == '#':
            return -1
        visited = set()
        res = []
        while queue:
            i, j, path = queue.popleft()
            if (i, j) == target:
                res = path
                break
            for x, y, d in [[i + 1, j, 'D'], [i - 1, j, 'U'], [i, j + 1, 'R'], [i, j - 1, 'L']]:
                if 0 <= x < n and 0 <= y < m and A[x][y] != '#' and (x, y) not in visited:
                    queue.append((x, y, path + [d]))
                    visited.add((x, y))
        return res


    n, m = list(map(int, input().split()))
    A = []
    for _ in range(n):
        A.append(list(input()))

    res = find(A)

    if not res:
        print("NO")
    else:
        print("YES")
        print(len(res))
        print(''.join(res))
