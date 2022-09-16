"""
There are n children who want to go to a Ferris wheel, and your task is to find a gondola for each child.

Each gondola may have one or two children in it, and in addition, the total weight in a gondola may not exceed x. 

You know the weight of every child.

What is the minimum number of gondolas needed for the children?

Input

The first input line contains two integers n and x: the number of children and the maximum allowed weight.

The next line contains n integers p1,p2,…,pn: the weight of each child.

Output

Print one integer: the minimum number of gondolas.

Constraints
1≤n≤2⋅105
1≤x≤109
1≤pi≤x
Example

Input:
4 10
7 2 3 9

Output:
3
"""


if __name__ == '__main__':
    n, max_weight = list(map(int, input().split()))
    A = list(map(int, input().split()))

    A.sort()
    i, j = 0, len(A) - 1
    res = 0
    pairs = [False] * n

    while i < j:
        if i != j and A[i] + A[j] <= max_weight:
            pairs[i] = pairs[j] = True
            res += 1
            i, j = i + 1, j - 1
        else:
            j -= 1

    print(res + sum([1 for x in pairs if not x]))
    
    