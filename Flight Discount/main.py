"""
Your task is to find a minimum-price flight route from Syrjälä to Metsälä.
You have one discount coupon, using which you can halve the price of any single flight during the route.

However, you can only use the coupon once.

Input

The first input line has two integers n and m: the number of cities and flight connections.
The cities are numbered 1,2,…,n. City 1 is Syrjälä, and city n is Metsälä.

After this there are m lines describing the flights.
Each line has three integers a, b, and c: a flight begins at city a, ends at city b, and its price is c.
Each flight is unidirectional.

You can assume that it is always possible to get from Syrjälä to Metsälä.

Output

Print one integer: the price of the cheapest route from Syrjälä to Metsälä.

When you use the discount coupon for a flight whose price is x, its price becomes ⌊x/2⌋ (it is rounded down to an integer).

Constraints
2≤n≤105
1≤m≤2⋅105
1≤a,b≤n
1≤c≤109
Example

Input:
3 4
1 2 3
2 3 1
1 3 7
2 1 5

Output:
2
"""
import collections
import heapq
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

    def dijkstra(adj, start_v):
        queue = [(0, start_v)]
        dist = [float('inf')] * n
        dist[start_v] = 0

        while queue:
            weight, v = heapq.heappop(queue)
            weight = -1 * weight

            for u, w in adj[v]:
                if dist[u] > w + weight:
                    dist[u] = w + weight
                    heapq.heappush(queue, (-dist[u], u))
        return dist

    n, m = mp()
    adj = collections.defaultdict(list)
    adj2 = collections.defaultdict(list)
    for _ in range(m):
        v, u, w = mp()
        adj[v - 1].append([u - 1, w])
        adj2[u - 1].append([v - 1, w])

    """
    run two Dijkstra from start and from the end  
    Loop in edges and get min(front_dijkstra[u] + w/2 + rev_dijkstra[v]);
    """
    front_dijkstra = dijkstra(adj, 0)
    rev_dijkstra = dijkstra(adj2, n - 1)

    res = float('inf')

    for v in range(n):
        for u, w in adj[v]:
            res = min(res, front_dijkstra[v] + rev_dijkstra[u] + (w // 2))

    print(res)
