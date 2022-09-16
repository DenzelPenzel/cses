"""
Given an array of n integers, your task is to find for each array position the nearest position to its left having a smaller value.

Input

The first input line has an integer n: the size of the array.

The second line has n integers x1,x2,…,xn: the array values.

Output

Print n integers: for each array position the nearest position with a smaller value. If there is no such position, print 0.

Constraints
1≤n≤2⋅105
1≤xi≤109
Example

Input:
8
2 5 1 4 8 3 2 5

Output:
0 1 0 3 4 3 3 7
"""

if __name__ == '__main__':
    n = int(input().split()[0])
    A = list(map(int, input().split()))

    st = []  # (val, idx)
    res = [0] * len(A)

    for i in range(len(A)):
        while st and st[-1][0] >= A[i]:
            st.pop()
        if st:
            res[i] = st[-1][1]
        st.append((A[i], i + 1))

    print(*res)
