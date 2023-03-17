"""
There are n
 cities and m
 flight connections between them. You want to travel from Syrjälä to Lehmälä so that you visit each city exactly once.
 How many possible routes are there?

Input

The first input line has two integers n and m: the number of cities and flights.
The cities are numbered 1,2,…,n. City 1 is Syrjälä, and city n is Lehmälä.

Then, there are m lines describing the flights.
Each line has two integers a and b: there is a flight from city a to city b.
All flights are one-way flights.

Output
Print one integer: the number of routes modulo 109+7.

Constraints
    2≤n≤20
    1≤m≤n2
    1≤a,b≤n

Example

Input:
    4 6
    1 2
    1 3
    2 3
    3 2
    2 4
    3 4

Output:
    2
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
    n, m = mp()
    adj = [[0] * n for _ in range(n)]
    MOD = int(1e9) + 7

    for _ in range(m):
        a, b = mp()
        adj[a - 1][b - 1] += 1

    # dp[i][mask]: number of routes that visit exactly the cities in the mask and end at city i
    dp = [[0] * n for _ in range(1 << n)]
    dp[1][0] = 1  # base case: starting from city 1 with only city 1 visited

    for mask in range(2, (1 << n)):
        if mask >> (n - 1) & 1 and mask != ((1 << n) - 1):
            continue
        for i in range(n):
            # check if city i is in the current mask
            if mask & (1 << i) != 0:
                prev_mask = mask ^ (1 << i)
                for j in range(n):
                    # check if city j is in the prev mask and is reachable from city i
                    if (prev_mask & 1 << j) != 0 and adj[j][i]:
                        dp[mask][i] += dp[prev_mask][j] * adj[j][i]
                        dp[mask][i] %= MOD

    # final answer: number of routes that visit all cities and end at city n
    ans = dp[(1 << n) - 1][n - 1]

    print(ans)
