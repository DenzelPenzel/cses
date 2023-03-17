"""
Byteland has n cities, and m roads between them.
The goal is to construct new roads so that there is a route between any two cities.

Your task is to find out the minimum number of roads required, and also determine which roads should be built.

Input

The first input line has two integers n and m: the number of cities and roads. The cities are numbered 1,2,…,n.

After that, there are m lines describing the roads. Each line has two integers a and b: there is a road between those cities.

A road always connects two different cities, and there is at most one road between any two cities.

Output

First print an integer k: the number of required roads.

Then, print k lines that describe the new roads. You can print any valid solution.

Constraints
1≤n≤105
1≤m≤2⋅105
1≤a,b≤n
Example

Input:
4 2
1 2
3 4

Output:
1
2 3
"""
import collections

if __name__ == '__main__':
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    def relax():
        for v in range(1, n + 1):
            find(v)
    n, m = list(map(int, input().split()))
    items = []
    for _ in range(m):
        items.append(list(map(int, input().split())))
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i
    for x, y in items:
        xx = find(x)
        yy = find(y)
        if xx != yy:
            parent[yy] = xx

    relax()

    comp = list(set(parent[1:]))

    print(len(comp) - 1)

    for y1, y2 in zip(comp, comp[1:]):
        print(*[y1, y2])
