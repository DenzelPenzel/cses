"""
The edit distance between two strings is the minimum number of operations required to transform one string into the other.

The allowed operations are:
Add one character to the string.
Remove one character from the string.
Replace one character in the string.
For example, the edit distance between LOVE and MOVIE is 2, because you can first replace L with M, and then add I.

Your task is to calculate the edit distance between two strings.

Input

The first input line has a string that contains n characters between A–Z.

The second input line has a string that contains m characters between A–Z.

Output

Print one integer: the edit distance between the strings.

Constraints
1≤n,m≤5000
Example

Input:
LOVE
MOVIE

Output:
2
"""

if __name__ == '__main__':
    word1 = input()
    word2 = input()

    n, m = len(word1) + 1, len(word2) + 1
    dp = [[0] * m for _ in range(n)]

    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + 1

    for i in range(1, m):
        dp[0][i] = dp[0][i - 1] + 1

    for i in range(1, n):
        for j in range(1, m):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    print(dp[n - 1][m - 1])

