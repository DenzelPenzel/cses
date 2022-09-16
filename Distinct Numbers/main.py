"""
You are given a list of n integers, and your task is to calculate the number of distinct values in the list.

Input

The first input line has an integer n: the number of values.

The second line has n integers x1,x2,…,xn.

Output

Print one integers: the number of distinct values.

Constraints
1≤n≤2⋅105
1≤xi≤109
Example

Input:
5
2 3 2 2 3

Output:
2
"""

from typing import List


def test(n: int, A: List[int]):
    return len(set(A))


if __name__ == '__main__':
    x = input().split()
    y = list(map(int, input().split()))
    print(test(int(x[0]), y))