"""
Time limit: 1.00 s Memory limit: 512 MB
You are given an array of n integers. Your task is to calculate for each window of k elements, from left to right, the minimum total cost of making all elements equal.

You can increase or decrease each element with cost x where x is the difference between the new and the original value. The total cost is the sum of such costs.

Input

The first input line contains two integers n and k: the number of elements and the size of the window.

Then there are n integers x1,x2,…,xn: the contents of the array.

Output

Output n−k+1 values: the costs.

Constraints
1≤k≤n≤2⋅105
1≤xi≤109
Example

Input:
8 3
2 4 3 5 8 1 2 1

Output:
2 2 5 7 7 1
"""

import heapq

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))

    # Two heaps (lo, hi) solution, keep the sum of the each heap (lo_sum, hi_sum)

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
