"""
Your task is to calculate the number of trailing zeros in the factorial n!.

For example, 20! = 2432902008176640000 and it has 4 trailing zeros.

Input

The only input line has an integer n.

Output

Print the number of trailing zeros in n!.

Constraints
1≤n≤109
Example

Input:
20

Output:
4
"""

if __name__ == '__main__':
    n = (int(input()))
    if n <= 4:
        print(0)
    else:
        res = 0
        k = 5
        while True:
            x = n // k
            if x <= 0: break
            res += x
            k *= 5
        print(res)
