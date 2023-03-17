"""
There are n projects you can attend. For each project, you know its starting and ending days and the amount of
money you would get as reward. You can only attend one project during a day.

What is the maximum amount of money you can earn?

Input

The first input line contains an integer n: the number of projects.

After this, there are n lines. Each such line has three integers ai, bi, and pi: the starting day, the ending day, and the reward.

Output

Print one integer: the maximum amount of money you can earn.

Constraints
1≤n≤2⋅105
1≤ai≤bi≤109
1≤pi≤109
Example

Input:
4
2 4 4
3 6 6
6 8 2
5 7 3

Output:
7

"""

if __name__ == '__main__':
    # find max non intersect intervals
    n = int(input())
    A = []
    for i in range(n):
        A.append(list(map(int, input().split())))

    A.sort(key=lambda x: x[0])
    dp = [x[2] for x in A]  # maximum amount of money we can earn before day i

    for i in range(n):
        a, b = A[i][0], A[i][1]
        max_val = 0
        for j in range(i):
            d, e = A[j][0], A[j][1]
            if a > e:
                max_val = max(max_val, dp[i] + dp[j])
        dp[i] = max(dp[i], max_val)

    print(max(dp))
