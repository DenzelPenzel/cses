"""
Time limit: 1.00 s Memory limit: 512 MB
You are given an array that contains each number between 1…n exactly once. Your task is to collect the numbers from 1 to n in increasing order.

On each round, you go through the array from left to right and collect as many numbers as possible. What will be the total number of rounds?

Input

The first line has an integer n: the array size.

The next line has n integers x1,x2,…,xn: the numbers in the array.

Output

Print one integer: the number of rounds.

Constraints
1≤n≤2⋅105
Example

Input:
5
4 2 1 5 3

Output:
3
"""

import bisect
from typing import List

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    seen = set()
    res = 1

    for x in A:
        if x + 1 in seen:
            res += 1
        seen.add(x)

    print(res)
