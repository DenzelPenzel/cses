"""
There are n apples with known weights. Your task is to divide the apples into two groups so that
the difference between the weights of the groups is minimal.

Input

The first input line has an integer n: the number of apples.

The next line has n integers p1,p2,…,pn: the weight of each apple.

Output

Print one integer: the minimum difference between the weights of the groups.

Constraints
1≤n≤20
1≤pi≤109
Example

Input:
5
3 2 7 4 1

Output:
1

Explanation: Group 1 has weights 2, 3 and 4 (total weight 9), and group 2 has weights 1 and 7 (total weight 8).
"""

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    if n <= 1:
        print(A[0])
    else:
        total = sum(A)
        used = [False] * len(A)
        res = float('inf')
        def DFS(i, curr):
            global res
            if i >= len(A) and curr != total:
                xx = total - curr
                res = min(res, abs(total - 2*curr))
                return
            for j in range(i, len(A)):
                if used[j]: continue
                curr += A[j]
                used[j] = True
                DFS(j + 1, curr)
                curr -= A[j]
                used[j] = False
        DFS(0, 0)
        print(res)

"""
10
603 324 573 493 659 521 654 70 718 257
"""
