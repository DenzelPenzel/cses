"""
In a movie festival, n movies will be shown. Syrjälä's movie club consists of k members, who will be all attending the festival.

You know the starting and ending time of each movie. 

What is the maximum total number of movies the club members can watch entirely if they act optimally?

Input

The first input line has two integers n and k: the number of movies and club members.

After this, there are n lines that describe the movies. Each line has two integers a and b: the starting and ending time of a movie.

Output

Print one integer: the maximum total number of movies.

Constraints
1≤k≤n≤2⋅105
1≤a<b≤109
Example

Input:
5 2
1 5
8 10
3 6
2 5
6 9

Output:
4
"""

from sys import stdin
from typing import List
import bisect
from utils.read_write_io import IOWrapper
import sys

# (sort by end + max heap queue)

if __name__ == '__main__':
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    input = lambda: list(map(int, sys.stdin.readline().rstrip("\n").split(" ")))
    n, k = input()
    A = sorted([input() for _ in range(n)], key=lambda x: x[1])

    res = 0
    available = [0] * k

    for start, end in A:
        idx = bisect.bisect_right(available, start)
        if idx == 0:
            continue
        del available[idx - 1]
        bisect.insort_left(available, end)
        res += 1

    print(res)