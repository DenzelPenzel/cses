"""
You are given an array that contains each number between 1…n exactly once. Your task is to collect the numbers from 1 to n in increasing order.

On each round, you go through the array from left to right and collect as many numbers as possible.

Given m operations that swap two numbers in the array, your task is to report the number of rounds after each operation.

Input

The first line has two integers n and m: the array size and the number of operations.

The next line has n integers x1,x2,…,xn: the numbers in the array.

Finally, there are m lines that describe the operations. Each line has two integers a and b: the numbers at positions a and b are swapped.

Output

Print m integers: the number of rounds after each swap.

Constraints
1≤n,m≤2⋅105
1≤a,b≤n
Example

Input:
5 3
4 2 1 5 3
2 3
1 5
2 3

Output:
2
3
4
"""

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    A = list(map(lambda x: int(x) - 1, input().split()))

    swaps = []
    tmp = []

    def add(i):
        if A[i] > 0:
            tmp.append((A[i] - 1, A[i]))
        if A[i] < n - 1:
            tmp.append((A[i], A[i] + 1))

    for _ in range(m):
        x, y = list(map(int, input().split()))
        swaps.append((x - 1, y - 1))

    mapping = {v: i for i, v in enumerate(A)}
    res = 1

    for i in range(1, len(A)):
        res += A[i] < A[i - 1]

    for i, j in swaps:
        add(i), add(j)

        for a, b in tmp:
            res -= mapping[b] < mapping[a]

        mapping[i], mapping[j] = mapping[i], mapping[j]
        A[i], A[j] = A[j], A[i]

        for a, b in tmp:
            res += mapping[b] < mapping[a]

        tmp.clear()
        print(res)
