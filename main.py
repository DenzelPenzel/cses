import bisect
import heapq
from itertools import accumulate
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
    n, L, R = list(map(int, raw[0]))
    A = list(map(int, raw[1]))

    # =============================================
    res = float('-inf')
    prefix = [0] + list(accumulate(A))

    for i in range(L, n + 1):
        for k in range(L, R + 1):
            if i - k >= 0:
                sub = A[i - k:i]
                res = max(res, prefix[i] - prefix[i - k])
                #print(sub, prefix[i] - prefix[i - k])
    print(res)



"""
First calculate prefix sum of array in array pre[].
Next iterate over the range L to N -1, and consider all subarray of size L to R.
"""
