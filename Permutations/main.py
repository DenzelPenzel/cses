"""
A permutation of integers 1,2,…,n is called beautiful if there are no adjacent elements whose difference is 1.

Given n, construct a beautiful permutation if such a permutation exists.

Input

The only input line contains an integer n.

Output

Print a beautiful permutation of integers 1,2,…,n. If there are several solutions, you may print any of them. 

If there are no solutions, print "NO SOLUTION".

Constraints
1≤n≤106
Example 1

Input:
5

Output:
4 2 5 3 1

Example 2

Input:
3

Output:
NO SOLUTION
"""

if __name__ == '__main__':
    def fn(n):
        if n == 1: return [1]
        if n in [2, 3]: return []
        if n == 4: return [2, 4, 1, 3]
        m = n // 2
        res = []
        for i in range(1, m + 1):
            res.append(i)
            res.append(n - i + 1)
        if n % 2 != 0:
            res.append(i + 1)
        res[0], res[-1] = res[-1], res[0]
        return res

    res = fn(int(input()))
    if not res:
        print("NO SOLUTION")
    else:
        print(*res)
