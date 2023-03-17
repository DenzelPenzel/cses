"""
Your task is to calculate the number of bit strings of length n.

For example, if n=3, the correct answer is 8, because the possible bit strings are 000, 001, 010, 011, 100, 101, 110, and 111.

Input

The only input line has an integer n.

Output

Print the result modulo 109+7.

Constraints
1≤n≤106
Example

Input:
3

Output:
8
"""

if __name__ == '__main__':
    N = int(input())
    mod = 10 ** 9 + 7


    def find(x: int, y: int) -> int:
        res = 1
        x = x % mod
        while y > 0:
            # if y is odd
            if y & 1:
                res = res * x % mod
            y = y >> 1
            x = (x * x) % mod
        return res


    x = find(2, N)
    print(2 ** N % mod == x, x)
