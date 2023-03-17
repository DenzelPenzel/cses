"""
A Gray code is a list of all 2n bit strings of length n,
where any two successive strings differ in exactly one bit (i.e., their Hamming distance is one).

Your task is to create a Gray code for a given length n.

Input

The only input line has an integer n.

Output

Print 2n lines that describe the Gray code. You can print any valid solution.

Constraints
1≤n≤16
Example

Input:
2

Output:
00
01
11
10

1        1
2        3
3        2
4        6
5        7
6        5
7        4
8        12
9        13
10       15
11       14
12       10
13       11
14

"""
import math

if __name__ == '__main__':
    limit = int(input())
    res = [0, 1, 3, 2]
    i = 2
    def fn(x: int):
        return int(math.log2(x)) + 1 <= limit
    while True:
        if i == len(res):
            break
        if i % 2 != 0:
            if fn(res[i] * 2 + 1): res.append(res[i] * 2 + 1)
            if fn(res[i] * 2): res.append(res[i] * 2)
        else:
            if fn(res[i] * 2): res.append(res[i] * 2)
            if fn(res[i] * 2 + 1): res.append(res[i] * 2 + 1)
        i += 1

    for x in res:
        print(bin(x)[2:].rjust(limit, '0'))