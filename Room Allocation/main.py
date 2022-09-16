"""
There is a large hotel, and n customers will arrive soon. Each customer wants to have a single room.

You know each customer's arrival and departure day. Two customers can stay in the same room if the departure day of the first customer is earlier than the arrival day of the second customer.

What is the minimum number of rooms that are needed to accommodate all customers? And how can the rooms be allocated?

Input

The first input line contains an integer n: the number of customers.

Then there are n lines, each of which describes one customer. Each line has two integers a and b: the arrival and departure day.

Output

Print first an integer k: the minimum number of rooms required.

After that, print a line that contains the room number of each customer in the same order as in the input. The rooms are numbered 1,2,…,k. You can print any valid solution.

Constraints
1≤n≤2⋅105
1≤a≤b≤109
Example

Input:
3
1 2
2 4
4 4

Output:
2
1 2 1
"""

import collections
import heapq

if __name__ == '__main__':
    n = int(input())
    A = []
    for k in range(n):
        x, y = list(map(int, input().split()))
        A.append((x, y, k))

    rooms = 0
    assign = [None] * len(A)
    room_id = 1
    A.sort(key=lambda x: x[0])

    used = []
    free = []

    heapq.heappush(used, (A[0][1], room_id))

    assign[A[0][2]] = room_id

    for i in range(1, len(A)):
        start, end, idx = A[i]
        while used and used[0][0] < start:
            heapq.heappush(free, heapq.heappop(used))
            
        if free and free[0][0] < start:
            _, x = heapq.heappop(free)
            heapq.heappush(used, (A[i][1], x))
            assign[idx] = x
        else:
            room_id += 1
            heapq.heappush(used, (A[i][1], room_id)) # end_time, room_id
            assign[idx] = room_id
            
        rooms = max(rooms, len(used))

    print(rooms)
    print(*assign)