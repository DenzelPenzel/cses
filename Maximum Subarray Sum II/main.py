"""
Given an array of n integers, your task is to find the maximum sum of values in a 
contiguous subarray with length between a and b.

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

import collections
from itertools import accumulate

if __name__ == '__main__':
    n, L, R = [8, 3, 6]  # list(map(int, input().split()))
    A = [2, 4, -4, 9, 87, 87, 87, -10000]  # list(map(int, input().split()))

    prefix = [0] + list(accumulate(A))
    stack = collections.deque([[0, 0]])
    res = prefix[n] if L == n else float('-inf')

    # we are trying to maximize (prefix[i] - prefix[j])
    # then we need to minimize  prefix[j] and j should be in the range [i - R, i]
    for i in range(L, len(A) + 1):
        # keep mono increasing stack
        while stack and stack[-1][0] > prefix[i - L]:
            stack.pop()

        while stack and i - stack[0][1] > R:
            stack.popleft()

        # adding the prefix[j] in the stack
        stack.append((prefix[i - L], i - L))
        # find the max sum in the range [j, i]
        res = max(res, prefix[i] - stack[0][0])

    print(res)
