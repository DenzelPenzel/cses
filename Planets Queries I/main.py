"""
You are playing a game consisting of n planets. Each planet has a teleporter to another planet (or the planet itself).

Your task is to process q queries of the form: when you begin on planet x and travel through k teleporters, which planet will you reach?

Input

The first input line has two integers n and q: the number of planets and queries. The planets are numbered 1,2,…,n.

The second line has n integers t1,t2,…,tn: for each planet, the destination of the teleporter. It is possible that ti=i.

Finally, there are q lines describing the queries.
Each line has two integers x and k: you start on planet x and travel through k teleporters.

Output

Print the answer to each query.

Constraints
1≤n,q≤2⋅105
1≤ti≤n
1≤x≤n
0≤k≤109
Example

Input:
4 3
2 1 1 4
1 2
3 4
4 1

Output:
1
2
4
"""

import collections
import os
import sys


def read_file(fname: str):
    with open(fname, mode='r') as f:
        content = f.readlines()
        context = [list(map(int, x.strip().split(' '))) for x in content]
    return context


if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')


def mp(): return map(int, sys.stdin.readline().split())


from typing import List

if __name__ == '__main__':
    class TreeAncestor:
        # Binary Lifting implementation
        # where dp[node][d] - equal to the d-th ancestor of node
        def __init__(self, n: int, parent: List[int]):
            self.dp = [[-1] * 30 for _ in range(n)]
            for j in range(30):
                for i in range(n):
                    if j == 0:
                        self.dp[i][0] = parent[i]  # 2^0 parent
                    elif self.dp[i][j - 1] != -1:
                        self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]

        def getKthAncestor(self, node: int, k: int) -> int:
            """
             we test if we jump in powers of two by using the & operator.
             If the i-th bit on the right is toggled, then we jump.
             For example, a jump of 13 would correspond to the binary number 1101
             We would jump 3 times on bits 0, 2, 3 (in that order) counting from the right.
            """
            # where 30 max lvl of ancestors
            for i in range(30):
                if k & (1 << i):
                    node = self.dp[node][i]
                    if node == -1:
                        return -1
            return node


    n, q = mp()
    mod = 10 ** 9 + 7
    graph = collections.defaultdict(list)
    inf = float('inf')
    parent = [None] * n

    for i, x in enumerate(mp()):
        parent[i] = x - 1

    tree = TreeAncestor(n, parent)
    for _ in range(q):
        node, k = mp()
        res = tree.getKthAncestor(node - 1, k)
        print(res + 1)
