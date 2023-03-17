"""
You are going to travel from Syrjälä to Lehmälä by plane. You would like to find answers to the following questions:

what is the minimum price of such a route?
how many minimum-price routes are there? (modulo 109+7)
what is the minimum number of flights in a minimum-price route?
what is the maximum number of flights in a minimum-price route?

Input

The first input line contains two integers n and m: the number of cities and the number of flights.
The cities are numbered 1,2,…,n. City 1 is Syrjälä, and city n is Lehmälä.

After this, there are m lines describing the flights.
Each line has three integers a, b, and c: there is a flight from city a to city b with price c.
All flights are one-way flights.

You may assume that there is a route from Syrjälä to Lehmälä.

Output

Print four integers according to the problem statement.

Constraints
1≤n≤105
1≤m≤2⋅105
1≤a,b≤n
1≤c≤109
Example

Input:
4 5
1 4 5
1 2 4
2 4 5
1 3 2
3 4 3

Output:
5 2 1 2
"""

import collections
import os
import sys
import heapq


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
    mod = 10**9 + 7
    graph = collections.defaultdict(list)
    seen = set()
    inf = float('inf')
    dist = [inf] * n
    total_ways = [1] * n
    min_dist = [inf] * n
    max_dist = [0] * n

    for _ in range(m):
        v, u, w = mp()
        graph[v - 1].append((u - 1, w))

    start = 0
    queue = [(0, start)]
    dist[start] = min_dist[start] = max_dist[start] = 0
    total_ways[start] = 1

    while queue:
        w, v = heapq.heappop(queue)

        if v in seen:
            continue

        seen.add(v)

        for u, ww in graph[v]:
            next_w = w + ww
            if dist[u] > next_w:
                dist[u] = next_w
                total_ways[u] = total_ways[v]
                min_dist[u] = min_dist[v] + 1
                max_dist[u] = max_dist[v] + 1
                heapq.heappush(queue, (next_w, u))
            elif dist[u] == next_w:
                total_ways[u] = (total_ways[u] + total_ways[v]) % mod
                min_dist[u] = min(min_dist[u], min_dist[v] + 1)
                max_dist[u] = max(max_dist[u], max_dist[v] + 1)

    print(dist[n - 1], total_ways[n - 1], min_dist[n - 1], max_dist[n - 1])
