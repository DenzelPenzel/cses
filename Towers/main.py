"""
You are given n cubes in a certain order, and your task is to build towers using them. 

Whenever two cubes are one on top of the other, the upper cube must be smaller than the lower cube.

You must process the cubes in the given order. 

You can always either place the cube on top of an existing tower, or begin a new tower. 

What is the minimum possible number of towers?

Input

The first input line contains an integer n: the number of cubes.

The next line contains n integers k1,k2,…,kn: the sizes of the cubes.

Output

Print one integer: the minimum number of towers.

Constraints
1≤n≤2⋅105
1≤ki≤109
Example

Input:
5
3 8 2 1 5

Output:
2
"""

import collections

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    res = 1
    current = A[0]

    for i in range(1, len(A)):
        if current <= A[i]:
            res += 1
            current = A[i]

    print(res)
