"""
You are given an array of n integers, and your task is to find three values (at distinct positions) whose sum is x.

Input

The first input line has two integers n and x: the array size and the target sum.

The second line has n integers a1,a2,…,an: the array values.

Output

Print three integers: the positions of the values. If there are several solutions, you may print any of them. If there are no solutions, print IMPOSSIBLE.

Constraints
1≤n≤5000
1≤x,ai≤109
Example

Input:
4 8
2 7 5 1

Output:
1 3 4
"""

if __name__ == '__main__':
    n, target = list(map(int, input().split()))
    A = list(map(int, input().split()))
    res = None
    seen = set()

    for i in range(len(A)):
        if A[i] not in seen:
            seen.add(A[i])
            x = target - A[i]
            mapping = {}
            for j, v in enumerate(A):
                if i == j: continue
                if x - v in mapping:
                    res = [i + 1, mapping[x - v] + 1, j + 1]
                    break
                mapping[A[j]] = j

            if res is not None:
                break

    if res is not None:
        print(*res)
    else:
        print('IMPOSSIBLE')