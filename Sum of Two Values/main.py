"""
You are given an array of n integers, and your task is to find two values (at distinct positions) whose sum is x.

Input

The first input line has two integers n and x: the array size and the target sum.

The second line has n integers a1,a2,…,an: the array values.

Output

Print two integers: the positions of the values. If there are several solutions, you may print any of them. If there are no solutions, print IMPOSSIBLE.

Constraints
1≤n≤2⋅105
1≤x,ai≤109
Example

Input:
4 8
2 7 5 1

Output:
2 4
"""
if __name__ == '__main__':
    n, target = list(map(int, input().split()))
    A = list(map(int, input().split()))
    mapping = {}
    prefix = 0
    found = False
    for i, x in enumerate(A):
        if target - x in mapping:
            res = [mapping.get(target - x), i + 1]
            found = True
            break
        mapping[x] = i + 1
    if not found:
        print("IMPOSSIBLE")
    else:
        print(*res)
