"""
Given n ranges, your task is to count for each range how many other ranges it contains and how many other ranges contain it.

Range [a,b] contains range [c,d] if a≤c and d≤b.

Input

The first input line has an integer n: the number of ranges.

After this, there are n lines that describe the ranges. Each line has two integers x and y: the range is [x,y].

You may assume that no range appears more than once in the input.

Output

First print a line that describes for each range (in the input order) how many other ranges it contains.

Then print a line that describes for each range (in the input order) how many other ranges contain it.

Constraints
1≤n≤2⋅105
1≤x<y≤109
Example

Input:
4
1 6
2 4
4 8
3 6

Output:
2 0 0 0
0 1 0 1
"""

import bisect


if __name__ == '__main__':
    n = int(input())
    A = []
    for k in range(n):
        x, y = list(map(int, input().split()))
        A.append((x, y, k))

    A.sort(key=lambda x: (x[0], -x[1]))

    self_contain = [0] * len(A)  # it contains some other range
    other_contain = [0] * len(A)  # if some other range contains it

    m = len(A)
    sorted_y = [] # could be improve to the Indexed tree
    for i in range(m - 1, -1, -1):
        y = A[i][1]
        if not sorted_y:
            sorted_y.append(y)
        else:
            pos = bisect.bisect_right(sorted_y, y)
            self_contain[A[i][2]] = pos
            sorted_y.insert(pos  s, y)

    sorted_y = []
    for i in range(m):
        y = A[i][1]
        if not sorted_y:
            sorted_y.append(y)
        else:
            pos = bisect.bisect_left(sorted_y, y)
            other_contain[A[i][2]] = len(sorted_y) - pos
            sorted_y.insert(pos, y)

    print(*self_contain)
    print(*other_contain)
