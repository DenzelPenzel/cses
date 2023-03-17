"""
There are 88418 paths in a 7×7 grid from the upper-left square to the lower-left square.
Each path corresponds to a 48-character description consisting of characters D (down), U (up), L (left) and R (right).

For example, the path

corresponds to the description DRURRRRRDDDLUULDDDLDRRURDDLLLLLURULURRUULDLLDDDD.

You are given a description of a path which may also contain characters ? (any direction).
Your task is to calculate the number of paths that match the description.

Input

The only input line has a 48-character string of characters ?, D, U, L and R.

Output

Print one integer: the total number of paths.

Example

Input:
??????R??????U??????????????????????????LD????D?

Output:
201

"""
from typing import List
from typing import List

if __name__ == '__main__':
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and not visited[x][y]


    def DFS(i, j, idx):
        if (i, j) == (n - 1, 0):
            if idx >= n ** 2 - 1: return 1
            return 0
        ii = is_valid(i - 1, j) + is_valid(i + 1, j)
        jj = is_valid(i, j + 1) + is_valid(i, j - 1)

        if (ii == 0 and jj == 2) or (ii == 2 and jj == 0):
            return 0

        res = 0
        for x, y, d in [(i + 1, j, 'D'), (i - 1, j, 'U'), (i, j - 1, 'L'), (i, j + 1, 'R')]:
            if is_valid(x, y) and (A[idx] == d or A[idx] == '?'):
                visited[x][y] = True
                res += DFS(x, y, idx + 1)
                visited[x][y] = False
        return res


    n = 7
    A = input()
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    start_pos = (0, 0)
    x = DFS(*start_pos, 0)
    print(x)

# ===========BIT MASKS============
m = ["LURD?".index(c) for c in input()]

if m.count(4) == 48:
    print(88418)
    exit()

if [x // 4 for x in m].index(0) >= 24:
    m.reverse()
    for i in range(48):
        if m[i] == 0 or m[i] == 2: m[i] = 2 - m[i]

d = (-1, -8, 1, 8)
f = [0] * 64
for i in range(7, 64, 8):
    f[i] = 1
for i in range(56, 64):
    f[i] = 1

k = 0

s = [0 if m[0] == 4 else m[0]]
f[0], i = 1, 1
while i > 0:
    p, z = s[-1] >> 3, s[-1] & 7
    if z == 4:
        s.pop()
        i -= 1
        f[p] = 0
        continue
    s[-1] += 1 if m[i - 1] == 4 else 4 - z

    p1 = p + d[z]
    if f[p1]: continue
    if p1 == 48:
        if i == 48: k += 1
        continue

    p2 = p1 + d[z]
    mr = d[(z + 1) & 3]
    if f[p2] or f[p2 - mr] or f[p2 + mr]:
        if not (f[p - mr] and f[p1 - mr] and f[p2 - mr]):
            if not (f[p + mr] and f[p1 + mr] and f[p2 + mr]):
                continue

    s.append((p1 << 3) | (0 if m[i] == 4 else m[i]))
    f[p1] = 1
    i += 1

print(k)
