"""
You are given the arrival and leaving times of n customers in a restaurant.

What was the maximum number of customers in the restaurant at any time?

Input

The first input line has an integer n: the number of customers.

After this, there are n lines that describe the customers. 

Each line has two integers a and b: the arrival and leaving times of a customer.

You may assume that all arrival and leaving times are distinct.

Output
    Print one integer: the maximum number of customers.

Constraints
    1≤n≤2⋅105
    1≤a<b≤109
    Example

Input:
    3
    5 8
    2 4
    3 9

Output:
    2

"""

if __name__ == '__main__':
    n = list(map(int, input().split()))[0]
    pairs = []
    timeline = {}
    max_val = 0
    for _ in range(n):
        a, b = list(map(int, input().split()))
        max_val = max(b, max_val)
        timeline[a] = 1
        timeline[b] = -1

    res = 0
    p = 0

    for i in range(max_val + 1):
        if i in timeline:
            p += timeline[i]
            res = max(res, p)

    print(res)
