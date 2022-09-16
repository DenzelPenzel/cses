import bisect
import heapq
import os
import collections
import queue
from statistics import median
from sys import prefix
from tracemalloc import start
from typing import List


def read_file(fname: str):
    with open(fname, mode='r') as f:
        content = f.readlines()
        context = [list(map(int, x.strip().split(' '))) for x in content]
    return context


if __name__ == "__main__":
    dirname = os.path.dirname(os.path.abspath(__file__))
    input = os.path.join(dirname, 'text.txt')
    raw = read_file(input)
    n, k = list(map(int, raw[0]))
    A = list(map(int, raw[1]))

    # =============================================
    import sys

    if k == 1:
        print(*[0] * n)
        sys.exit()

    def switch(h1, h2):
        x, i = heapq.heappop(h1)
        heapq.heappush(h2, (-x, i))

        return abs(x)

    def get_cost(hi_sum, lo_sum, k):
        return hi_sum - lo_sum + median if k % 2 == 1 else hi_sum - lo_sum

    lo = []  # max heap [4,3,2]
    hi = []  # min heap [5,6,7] either equal lo or one greater lo

    lo_sum, hi_sum = 0, 0

    for i in range(k):
        heapq.heappush(lo, (-A[i], i))
        lo_sum += A[i]

    for _ in range(k // 2):
        x = switch(lo, hi)
        hi_sum += x
        lo_sum -= x

    median = -lo[0][0]
    ans = [get_cost(hi_sum, lo_sum, k)]

    for i in range(k, n):
        out_num = A[i - k]

        prev_hi_top = hi[0][0]

        heapq.heappush(hi, (A[i], i))
        hi_sum += A[i]

        x = switch(hi, lo)
        lo_sum += x
        hi_sum -= x

        if out_num >= prev_hi_top:
            hi_sum -= out_num
            x = switch(lo, hi)
            hi_sum += x
            lo_sum -= x
        else:
            lo_sum -= out_num

        # throw out invalid indices
        while hi and hi[0][1] <= i - k:
            heapq.heappop(hi)

        while lo and lo[0][1] <= i - k:
            heapq.heappop(lo)

        median = -lo[0][0]
        ans.append(get_cost(hi_sum, lo_sum, k))

    print(*ans)
