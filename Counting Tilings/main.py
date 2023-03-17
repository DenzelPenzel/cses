"""
Your task is to count the number of ways you can fill an n×m grid using 1×2 and 2×1 tiles.

Input

The only input line has two integers n and m.

Output

Print one integer: the number of ways modulo 109+7.

Constraints
1≤n≤10
1≤m≤1000
Example

Input:
4 7

Output:
781
"""
from typing import List

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    # [1, 2, 3, 4]
    res = 0


    def DFS(i, j, prev_state, state):
        global res

        print(i, j, prev_state, state)

        if i >= n:
            res += 1
            return

        if j >= m:
            DFS(i + 1, 0, state[:], [None] * m)
            return

        for k in [1, 2, 3, 4]:
            if k == 1 and i == n - 1: continue
            if k == 2 and (i == 0 or prev_state[j] != 1): continue
            if k == 3 and (j == m - 1 or prev_state[j] == 1): continue
            if k == 4 and (i - 1 >= 0 and state[j - 1] != 3 or j == 0 or prev_state[j] == 1): continue
            x = state[j]
            state[j] = k
            DFS(i, j + 1, prev_state, state)
            state[j] = x


    DFS(0, 0, [None] * m, [None] * m)

    print(res)
