"""
Given an array of n integers, your task is to count the number of subarrays where the sum of values is divisible by n.

Input

The first input line has an integer n: the size of the array.

The next line has n integers a1,a2,…,an: the contents of the array.

Output

Print one integer: the required number of subarrays.

Constraints
1≤n≤2⋅105
−109≤ai≤109

Example

Input:
5
3 1 2 7 4

Output:
1
"""

if __name__ == '__main__':
    n = list(map(int, input().split()))[0]
    A = list(map(int, input().split()))

    mapping = {0: 1}
    res = prefix = 0

    for x in A:
        prefix += x
        key = prefix % n

        if key in mapping:
            res += mapping[key]

        mapping[key] = mapping.get(key, 0) + 1

    print(res)