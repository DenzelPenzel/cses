"""


"""

if __name__ == '__main__':
    def DFS(i, j):
        for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
            if 0 <= x < n and 0 <= y < m and A[x][y] == '.':
                A[x][y] = '#'
                DFS(x, y)

    n, m = list(map(int, input().split()))
    A = []
    for _ in range(n):
        A.append(list(input()))
    res = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] == '.':
                A[i][j] = '#'
                DFS(i, j)
                res += 1
    print(res)

