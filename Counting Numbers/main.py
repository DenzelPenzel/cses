"""
Your task is to count the number of integers between $a$ and $b$ where no two adjacent digits are the same.

Input

The only input line has two integers $a$ and $b$.

Output

Print one integer: the answer to the problem.

Constraints
$0 \le a \le b \le 10^{18}$
Example

Input:
123 321

Output:
171
"""

if __name__ == '__main__':
    a, b = list(map(int, input().split()))
    res = 0
    for x in range(a, b + 1):
        num = list(str(x))
        if all(y1 != y2 for y1, y2 in zip(num, num[1:])):
            res += 1
    print(res)
