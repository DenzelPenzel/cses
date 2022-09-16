"""
Given an array of n positive integers, your task is to count the number of subarrays having sum x.

Input

The first input line has two integers n and x: the size of the array and the target sum x.

The next line has n integers a1,a2,…,an: the contents of the array.

Output

Print one integer: the required number of subarrays.

Constraints
1≤n≤2⋅105
1≤x,ai≤109
Example

Input:
5 7
2 4 1 2 7

Output:
3
"""

if __name__ == '__main__':
    n, target = list(map(int, input().split()))
    A = list(map(int, input().split()))

    mapping = {0: 1}
    res = prefix = 0

    for x in A:
        prefix += x

        if prefix - target in mapping:
            res += mapping[prefix - target]

        mapping[prefix] = mapping.get(prefix, 0) + 1

    print(res)
