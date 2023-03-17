"""
You have two coin piles containing a and b coins.
On each move, you can either remove one coin from the left pile and two coins from the right pile,
or two coins from the left pile and one coin from the right pile.

Your task is to efficiently find out if you can empty both the piles.

Input

The first input line has an integer t: the number of tests.

After this, there are t lines, each of which has two integers a and b: the numbers of coins in the piles.

Output

For each test, print "YES" if you can empty the piles and "NO" otherwise.

Constraints
1≤t≤105
0≤a,b≤109
Example

Input:
3
2 1
2 2
3 3

Output:
YES
NO
YES

Possible pairs equal to:
    (1, 2) 3
    (3, 3) 6
    (2, 4) 6
    (3, 6) 9
    (4, 5) 9
    (5, 7) 12
    (6, 6) 12
    (4, 8) 12
    (6, 9) 15
    (5, 10) 15
    (7, 8) 15
    (7, 11) 18
    (9, 9) 18
    (6, 12) 18
    (8, 10) 18
    (10, 11) 21
    (8, 13) 21
    (7, 14) 21
    (9, 12) 21
    (9, 15) 24
    (11, 13) 24
    (8, 16) 24
    (10, 14) 24
    (12, 12) 24
    (10, 17) 27
    (12, 15) 27
    (11, 16) 27
    (9, 18) 27
    (13, 14) 27
    (13, 17) 30

Sum of pairs is an arithmetic_progression with progression_diff = 3
"""

if __name__ == '__main__':
    n = int(input())
    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))

    for a, b in A:
        if (a == 0 and b == 0) or ((a + b) % 3 == 0 and max(a, b) // 2 <= min(a, b)):
            print("YES")
        else:
            print("NO")
