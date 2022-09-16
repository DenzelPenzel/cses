"""
Given an array of n integers, your task is to calculate the number of subarrays that have at most k distinct values.

Input

The first input line has two integers n and k.

The next line has n integers x1,x2,…,xn: the contents of the array.

Output

Print one integer: the number of subarrays.

Constraints
1≤k≤n≤2⋅105
1≤xi≤109
Example

Input:
5 2
1 2 3 1 1

Output:
10
"""

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))

    res = 0
    mapping = {}
    start, end = 0, 0
    cnt_unique = 0

    while end < len(A):
        if mapping.get(A[end], 0) == 0:
            cnt_unique += 1
        mapping[A[end]] = mapping.get(A[end], 0) + 1
        end += 1
        while cnt_unique > k:
            if mapping[A[start]] == 1:
                cnt_unique -= 1
            mapping[A[start]] -= 1
            start += 1
        res += end - start

    print(res)
