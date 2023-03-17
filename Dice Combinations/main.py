"""
Time limit: 1.00 s Memory limit: 512 MB
Your task is to count the number of ways to construct sum n by throwing a dice one or more times.
Each throw produces an outcome between 1 and 6.

For example, if n=3, there are 4 ways:
1+1+1
1+2
2+1
3
Input
The only input line has an integer n.

Output
Print the number of ways modulo 109+7.

Constraints
1≤n≤106
Example

Input:
3

Output:
4
"""

if __name__ == '__main__':
    # 0-1 Knapsack problem
    target = int(input())
    dp = [0] * (target + 1)
    dp[0] = 1
    mod = 10 ** 9 + 7
    for cur_sum in range(1, target + 1):
        for coin in range(1, 7):
            if cur_sum - coin >= 0:
                dp[cur_sum] = (dp[cur_sum] + dp[cur_sum - coin]) % mod
    print(dp[target] % mod)
