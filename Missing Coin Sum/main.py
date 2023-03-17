"""
You have n coins with positive integer values.

What is the smallest sum you cannot create using a subset of the coins?

Input

The first input line has an integer n: the number of coins.

The second line has n integers x1,x2,…,xn: the value of each coin.

Output

Print one integer: the smallest coin sum.

Constraints
1≤n≤2⋅105
1≤xi≤109
Example

Input:
5
2 9 1 2 7

Output:
6
"""

if __name__ == '__main__':
    """
    At any index i in a sorted array A, current_sum represents sum(A[ 0...i ])
    We can form every possible sum from 1...current_sum, when we are at index i 
    So the next possible smallest sum at index i can be current_sum + 1
    We can get current_sum + 1 as the answer if and only if A[i+1] > current_sum + 1, 
    otherwise we would be able to form subsets with sums from 1...(current_sum + A[i+1])
   (just add a[i+1] to all subsets which give sum 1...current_sum to get subsets giving sum 1...current_sum + A[i+1])
    """
    n = int(input())
    A = sorted(list(map(int, input().split())))
    current_sum = 0
    for i in range(len(A)):
        if current_sum + 1 < A[i]:
            break
        current_sum += A[i]
    print(current_sum + 1)
