"""
Your task is to find the k shortest flight routes from Syrjälä to Metsälä. A route can visit the same city several times.

Note that there can be several routes with the same price and each of them should be considered (see the example).

Input

The first input line has three integers n, m, and k: the number of cities, the number of flights, and the parameter k.
The cities are numbered 1,2,…,n. City 1 is Syrjälä, and city n is Metsälä.

After this, the input has m lines describing the flights.

Each line has three integers a, b, and c:
a flight begins at city a, ends at city b, and its price is c.

All flights are one-way flights.

You may assume that there are at least k distinct routes from Syrjälä to Metsälä.

Output

Print k integers: the prices of the k cheapest routes sorted according to their prices.

Constraints
2≤n≤105
1≤m≤2⋅105
1≤a,b≤n
1≤c≤109
1≤k≤10
Example

Input:
4 6 3
1 2 1
1 3 3
2 3 2
2 4 6
3 2 8
3 4 1

Output:
4 4 7

Explanation: The cheapest routes are 1→3→4 (price 4), 1→2→3→4 (price 4) and 1→2→4 (price 7).
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
    def dijkstra(adj, start_v, end_v):
        queue = [(0, start_v)]
        mapping = {v: [] for v in range(1, n + 1)}
        mapping[start_v].append(0)

        while queue:
            w, v = heapq.heappop(queue)
            w = -1 * w

            for u, c_w in adj[v]:
                ww = w + c_w
                weights = mapping[u]

                if len(mapping[u]) < k:
                    heapq.heappush(weights, -ww)
                    queue.append((-ww, u))
                else:
                    if -weights[0] > ww:
                        heapq.heappop(weights)
                        heapq.heappush(weights, -ww)
                        queue.append((-ww, u))

        return mapping[end_v]


    n, m, k = mp()
    graph = collections.defaultdict(list)

    for _ in range(m):
        v, u, w = mp()
        graph[v].append((u, w))

    top_k = dijkstra(graph, 1, n)

    print(*[-x for x in heapq.nlargest(k, top_k)])
