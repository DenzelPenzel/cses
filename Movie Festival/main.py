"""
In a movie festival n movies will be shown. You know the starting and ending time of each movie. 

What is the maximum number of movies you can watch entirely?

Input

The first input line has an integer n: the number of movies.

After this, there are n lines that describe the movies. Each line has two integers a and b: the starting and ending times of a movie.

Output

Print one integer: the maximum number of movies.

Constraints
1≤n≤2⋅105
1≤a<b≤109
Example

Input:
3
3 5
4 9
5 8

Output:
2
"""
from typing import List

if __name__ == '__main__':

    def longest_non_overlap(A: List[List[int]]) -> List[List[int]]:
        A.sort(key=lambda x: x[0])
        prev = None
        longest = 0
        for i in range(len(A)):
            if prev is None or prev <= A[i][0]:
                prev = A[i][1]
                longest += 1
            else:
                prev = min(prev, A[i][1])
        return longest

    n = list(map(int, input().split()))[0]
    intervals = []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        intervals.append([a, b])

    print(longest_non_overlap(intervals))
