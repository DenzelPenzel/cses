"""
You are given an integer n. On each step, you may subtract one of the digits from the number.

How many steps are required to make the number equal to 0?

Input

The only input line has an integer n.

Output

Print one integer: the minimum number of steps.

Constraints
1≤n≤106
Example

Input:
27

Output:
5

Explanation: An optimal solution is 27→20→18→10→9→0
"""

if __name__ == '__main__':
    def parse(x):
        res = []
        while x:
            d = x % 10
            x //= 10
            if d > 0: res.append(d)
        return res


    def fn(t: int) -> int:
        mapping = {i: 1 for i in range(1, 10)}
        if t <= 9: return mapping[t]
        for x in range(10, t + 1, 10):
            for xx in range(x, x + 10):
                min_val = float('inf')
                for xxx in parse(xx):
                    min_val = min(min_val, mapping[xx - xxx] + 1)
                mapping[xx] = min_val
                if xx == t:
                    return mapping[xx]
            mapping_copy = {}
            for k in range(x + 10 - max(parse(x + 10)), x + 10 + 1):
                if k in mapping:
                    mapping_copy[k] = mapping[k]
            mapping = mapping_copy
        return mapping[t]


    x = int(input())
    print(fn(x))
