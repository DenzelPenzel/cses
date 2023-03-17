"""
A factory has n machines which can be used to make products. Your goal is to make a total of t products.

For each machine, you know the number of seconds it needs to make a single product. The machines can work simultaneously, and you can freely decide their schedule.

What is the shortest time needed to make t products?

Input

The first input line has two integers n and t: the number of machines and products.

The next line has n integers k1,k2,…,kn: the time needed to make a product using each machine.

Output

Print one integer: the minimum time needed to make t products.

Constraints
1≤n≤2⋅105
1≤t≤109
1≤ki≤109
Example

Input:
3 7
3 2 5

Output:
8

Explanation: Machine 1 makes two products, machine 2 makes four products and machine 3 makes one product.

"""

from utils.read_write_io import IOWrapper
import sys

if __name__ == '__main__':
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

    input = lambda: list(map(int, sys.stdin.readline().rstrip("\n").split(" ")))

    n, t = input()
    A = input()

    lo, hi = 1, int(1e18)
    res = float('inf')

    while lo < hi:
        mid = lo + ((hi - lo) >> 1)

        cur_time = 0

        for x in A:
            cur_time += mid // x
            if cur_time >= t:
                break

        if cur_time < t:
            lo = mid + 1
        else:
            hi = mid

    print(lo)
