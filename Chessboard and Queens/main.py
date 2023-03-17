"""
Your task is to place eight queens on a chessboard so that no two queens are attacking each other.
As an additional challenge, each square is either free or reserved, and you can only place queens on the free squares.
However, the reserved squares do not prevent queens from attacking each other.

How many possible ways are there to place the queens?

Input

The input has eight lines, and each of them has eight characters. Each square is either free (.) or reserved (*).

Output

Print one integer: the number of ways you can place the queens.

Example

Input:
........
........
..*.....
........
........
.....**.
...*....
........

Output:
65
"""

from typing import List

if __name__ == '__main__':
    def is_valid(j_positions: List[int], new_j: int) -> bool:
        for i, j in enumerate(j_positions):
            abs_col_dist = abs(new_j - j)
            if abs_col_dist == 0 or abs_col_dist == len(j_positions) - i: return False
        return True

    n = 8
    A = []
    res = 0
    for _ in range(n): A.append(input())

    def DFS(i, rows):
        global res
        if i == n:
            res += 1
            return
        for new_j in range(n):
            if A[i][new_j] == '.' and is_valid(rows, new_j):
                rows.append(new_j)
                DFS(i + 1, rows)
                rows.pop()


    DFS(0, [])
    print(res)
