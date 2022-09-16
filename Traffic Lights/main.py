"""
There is a street of length x whose positions are numbered 0,1,…,x. Initially there are no traffic lights, but n sets of traffic lights are added to the street one after another.

Your task is to calculate the length of the longest passage without traffic lights after each addition.

Input

The first input line contains two integers x and n: the length of the street and the number of sets of traffic lights.

Then, the next line contains n integers p1,p2,…,pn: the position of each set of traffic lights. Each position is distinct.

Output

Print the length of the longest passage without traffic lights after each addition.

Constraints
1≤x≤109
1≤n≤2⋅105
0<pi<x
Example

Input:
8 3
3 6 2

Output:
5 3 3
"""

import bisect
import collections
import heapq

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    traffic_lights = list(map(int, input().split()))

    def get_longest_route():
        A = [0] + sorted(traffic_lights) + [n, 0]
        l = len(A) - 1
        ranges = {A[i]: [A[i - 1], A[i + 1]] for i in range(l)}
        max_range = max([A[i] - A[i - 1] for i in range(1, l)])
        """
              X X     X
         [0,0,0,0,0,0,0,0,0]
          0 1 2 3 4 5 6 7 8
        """
        res = [max_range]

        for x in traffic_lights[::-1]:
            l, r = ranges[x]
            max_range = max(max_range, r - l)
            ranges[l][1] = r
            ranges[r][0] = l
            res.append(max_range)

        print(*res[::-1][1:])

    def get_longest_route_II():
        queue = []
        seen = set()
        light_pos = [0, n]
        res = []

        for x in traffic_lights:
            idx = bisect.bisect_left(light_pos, x)

            light_pos.insert(idx, x)

            seen.add((light_pos[idx - 1], light_pos[idx + 1]))

            L = (light_pos[idx - 1], light_pos[idx])
            R = (light_pos[idx], light_pos[idx + 1])

            heapq.heappush(queue, (-(L[1] - L[0]), L))
            heapq.heappush(queue, (-(R[1] - R[0]), R))

            while queue and queue[0][1] in seen:
                heapq.heappop(queue)

            res.append(str(-queue[0][0]))

        print(*res)

    get_longest_route()
"""

     X X     X
[0,0,0,0,0,0,0,0,0]
 0 1 2 3 4 5 6 7 8

3 6 2
5 3 3





"""
