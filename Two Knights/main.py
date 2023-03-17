"""
Your task is to count for k=1,2,…,n the number of ways two knights can be placed on a k×k chessboard so that they do not attack each other.

Input

The only input line contains an integer n.

Output

Print n integers: the results.

Constraints
1≤n≤10000
Example

Input:
8

Output:
0
6
28
96
252
550
1056
1848
"""

if __name__ == '__main__':
    k = int(input())
    print(0)
    for length in range(2, k+1):
        # total ways to place two knights on the board
        total_ways = (length**2 * (length**2-1) / 2)
        # pos under 
        pos_under_attack = 4 * (length - 2) * (length - 1)
        print(int(total_ways - pos_under_attack))
    