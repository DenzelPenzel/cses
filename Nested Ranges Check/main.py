"""
Given n ranges, your task is to determine for each range if it contains some other range and if some other range contains it.

Range [a,b] contains range [c,d] if a≤c and d≤b.

Input

The first input line has an integer n: the number of ranges.

After this, there are n lines that describe the ranges. Each line has two integers x and y: the range is [x,y].

You may assume that no range appears more than once in the input.

Output

First print a line that describes for each range (in the input order) if it contains some other range (1) or not (0).

Then print a line that describes for each range (in the input order) if some other range contains it (1) or not (0).

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
1 0 0 0
0 1 0 1
"""

if __name__ == '__main__':
    n = int(input())
    A = []
    for k in range(n):
        x, y = list(map(int, input().split()))
        A.append((x, y, k))

    A.sort(key=lambda x: (x[0], -x[1]))

    self_contain = [0] * len(A)  # it contains some other range
    other_contain = [0] * len(A)  # if some other range contains it

    min_so_far = None

    for i in range(len(A) - 1, -1, -1):
        x, y, id = A[i]
        if min_so_far and min_so_far <= y:
            self_contain[id] = 1
        min_so_far = y if not min_so_far else min(min_so_far, y)

    max_so_far = None

    for x, y, id in A:
        if max_so_far and max_so_far >= y:
            other_contain[id] = 1
        max_so_far = y if not max_so_far else max(max_so_far, y)

    print(*self_contain)
    print(*other_contain)
