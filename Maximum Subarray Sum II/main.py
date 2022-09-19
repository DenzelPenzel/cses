"""
Given an array of n integers, your task is to find the maximum sum of values in a contiguous subarray with length between a and b.

Input

The first input line has three integers n, a and b: the size of the array and the minimum and maximum subarray length.

The second line has n integers x1,x2,…,xn: the array values.

Output

Print one integer: the maximum subarray sum.

Constraints
1≤n≤2⋅105
1≤a≤b≤n
−109≤xi≤109
Example

Input:
8 1 2
-1 3 -2 5 3 -5 2 2

Output:
8
"""

from itertools import accumulate


if __name__ == '__main__':
    n, L, R = list(map(int, input().split()))
    A = list(map(int, input().split()))

    res = float('-inf')
    prefix = [0] + list(accumulate(A))

    for i in range(L, n + 1):
        for k in range(L, R + 1):
            if i - k >= 0:
                sub = A[i - k:i]
                res = max(res, prefix[i] - prefix[i - k])
    print(res)
