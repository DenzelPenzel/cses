"""
A number spiral is an infinite grid whose upper-left square has number 1. 

Here are the first five layers of the spiral:

Your task is to find out the number in row y and column x.

Input

The first input line contains an integer t: the number of tests.

After this, there are t lines, each containing integers y and x.

Output

For each test, print the number in row y and column x.

Constraints
1≤t≤105
1≤y,x≤109
Example

Input:
3
2 3
1 1
4 2

Output:
8
1
15
"""

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        x, y = list(map(int, input().split()))
        res = None

        if x > y:
            if x % 2 != 0:
                res = (x - 1)**2 + y
            else:
                res = x**2 - y + 1
        else:
            if y % 2 != 0:
                res = y**2 - x + 1
            else:
                res = (y - 1)**2 + x

        print(res)
