"""
There are n sticks with some lengths. Your task is to modify the sticks so that each stick has the same length.

You can either lengthen and shorten each stick. Both operations cost x where x is the difference between the new and original length.

What is the minimum total cost?

Input

The first input line contains an integer n: the number of sticks.

Then there are n integers: p1,p2,…,pn: the lengths of the sticks.

Output

Print one integer: the minimum total cost.

Constraints
1≤n≤2⋅105
1≤pi≤109
Example

Input:
5
2 3 1 5 2

Output:
5
"""

if __name__ == '__main__':
    n = list(map(int, input().split()))[0]
    A = list(map(int, input().split()))
    A.sort()
    mid = len(A) // 2
    res = float('inf')
    x = 0
    for i in range(len(A)):
        x += abs(A[i] - A[mid])
    res = min(res, x)
    print(res)


