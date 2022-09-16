"""
There are n books, and Kotivalo and Justiina are going to read them all. For each book, you know the time it takes to read it.

They both read each book from beginning to end, and they cannot read a book at the same time. What is the minimum total time required?

Input

The first input line has an integer n: the number of books.

The second line has n integers t1,t2,…,tn: the time required to read each book.

Output

Print one integer: the minimum total time.

Constraints
1≤n≤2⋅105
1≤ti≤109
Example

Input:
3
2 8 3

Output:
16
"""

if __name__ == '__main__':
    n = int(input().split()[0])
    A = list(map(int, input().split()))

    max_value = max(A)
    total_sum = sum(A)

    print(max_value * 2 if max_value > (total_sum - max_value) else total_sum)

