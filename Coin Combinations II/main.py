"""
Consider a money system consisting of n coins. Each coin has a positive integer value.

Your task is to calculate the number of distinct ordered ways you can produce a money sum x using the available coins.

For example, if the coins are {2,3,5} and the desired sum is 9, there are 3 ways:
2+2+5
3+3+3
2+2+2+3

Input

The first input line has two integers n and x: the number of coins and the desired sum of money.

The second line has n distinct integers c1,c2,…,cn: the value of each coin.

Output

Print one integer: the number of ways modulo 109+7.

Constraints
1≤n≤100
1≤x≤106
1≤ci≤106
Example

Input:
3 9
2 3 5

Output:
3
"""

if __name__ == '__main__':
    n, target = list(map(int, input().split()))
    coins = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    dp = [0] * (target + 1)
    dp[0] = 1
    # get the number of unique combinations
    for coin in coins:
        for w in range(coin, target + 1):
            dp[w] = dp[w] + dp[w - coin]
            dp[w] %= mod
    print(dp[target])
