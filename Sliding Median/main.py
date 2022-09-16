"""
Time limit: 1.00 s Memory limit: 512 MB
You are given an array of n integers. Your task is to calculate the median of each window of k elements, from left to right.

The median is the middle element when the elements are sorted. If the number of elements is even, there are two possible medians and we assume that the median is the smaller of them.

Input

The first input line contains two integers n and k: the number of elements and the size of the window.

Then there are n integers x1,x2,…,xn: the contents of the array.

Output

Print n−k+1 values: the medians.

Constraints
1≤k≤n≤2⋅105
1≤xi≤109
Example

Input:
8 3
2 4 3 5 8 1 2 1

Output:
3 4 5 5 2 1
"""

import heapq
import collections


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))

    lo = []  # max heap [4,3,2]
    hi = []  # min heap [5,6,7] either equal lo or one greater lo

    for i in range(k):
        if len(lo) == len(hi):
            heapq.heappush(hi, -heapq.heappushpop(lo, -A[i]))
        else:
            heapq.heappush(lo, -heapq.heappushpop(hi, A[i]))

    ans = [hi[0]] if k & 1 else [min(hi[0], lo[0] * -1)]

    to_remove = collections.Counter()

    for i in range(k, len(A)):
        heapq.heappush(lo, -heapq.heappushpop(hi, A[i]))
        out_num = A[i - k]

        if out_num > -lo[0]:
            heapq.heappush(hi, -heapq.heappop(lo))

        to_remove[out_num] += 1

        while lo and to_remove[-lo[0]]:
            to_remove[-lo[0]] -= 1
            heapq.heappop(lo)

        while to_remove[hi[0]]:
            to_remove[hi[0]] -= 1
            heapq.heappop(hi)

        print(lo, hi)

        if k % 2 != 0:
            ans.append(hi[0])
        else:
            ans.append(min(hi[0], lo[0] * -1))

    print(*ans)
