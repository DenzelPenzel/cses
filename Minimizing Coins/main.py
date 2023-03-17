"""
Consider a money system consisting of n coins. Each coin has a positive integer value.

Your task is to produce a sum of money x using the available coins in such a way that the number of coins is minimal.

For example, if the coins are {1,5,7} and the desired sum is 11, an optimal solution is 5+5+1 which requires 3 coins.

Input

The first input line has two integers n and x: the number of coins and the desired sum of money.

The second line has n distinct integers c1,c2,…,cn: the value of each coin.

Output

Print one integer: the minimum number of coins. If it is not possible to produce the desired sum, print −1.

Constraints
1≤n≤100
1≤x≤106
1≤ci≤106
Example

Input:
3 11
1 5 7

Output:
3
"""

if __name__ == '__main__':
    inf = float('inf')
    n, target = list(map(int, input().split()))
    coins = list(sorted(map(int, input().split())))
    dp = [inf] * (target + 1)
    dp[0] = 0

    for cur_sum in range(1, target + 1):
        for coin in coins:
            if cur_sum < coin:
                break
            dp[cur_sum] = min(dp[cur_sum], dp[cur_sum - coin] + 1)

    print(-1 if dp[target] == inf else dp[target])
