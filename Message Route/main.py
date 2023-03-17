"""
Syrjälä's network has n computers and m connections. Your task is to find out if Uolevi can send a message to Maija, and if it is possible, what is the minimum number of computers on such a route.

Input

The first input line has two integers n and m: the number of computers and connections. The computers are numbered 1,2,…,n. Uolevi's computer is 1 and Maija's computer is n.

Then, there are m lines describing the connections. Each line has two integers a and b: there is a connection between those computers.

Every connection is between two different computers, and there is at most one connection between any two computers.

Output

If it is possible to send a message, first print k: the minimum number of computers on a valid route. After this, print an example of such a route. You can print any valid solution.

If there are no routes, print "IMPOSSIBLE".

Constraints
2≤n≤105
1≤m≤2⋅105
1≤a,b≤n
Example

Input:
5 5
1 2
1 3
1 4
2 3
5 4

Output:
3
1 4 5
"""
import collections
from typing import List

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    A = []
    for _ in range(m):
        A.append(list(map(int, input().split())))

    max_size = 10 ** 5 + 1
    graph = collections.defaultdict(list)
    dist = [float('inf')] * max_size
    queue = collections.deque([1])
    dist[1] = 0

    for x, y in A:
        graph[x].append(y)
        graph[y].append(x)

    has_path = False
    route = [None] * max_size

    while queue:
        v = queue.popleft()

        if v == n:
            has_path = True
            break

        for u in graph[v]:
            if dist[u] > dist[v] + 1:
                dist[u] = dist[v] + 1
                queue.append(u)
                # construct the route
                route[u] = v

    steps = dist[n]

    if steps == float('inf'):
        print('IMPOSSIBLE')
    else:
        path = [None] * (steps + 1)
        v = n
        # reconstruct the route to target
        for i in range(steps, -1, -1):
            path[i] = v
            v = route[v]

        print(steps + 1)
        print(*path)
