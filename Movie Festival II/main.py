"""
In a movie festival, n movies will be shown. Syrjälä's movie club consists of k members, who will be all attending the festival.

You know the starting and ending time of each movie. 

What is the maximum total number of movies the club members can watch entirely if they act optimally?

Input

The first input line has two integers n and k: the number of movies and club members.

After this, there are n lines that describe the movies. Each line has two integers a and b: the starting and ending time of a movie.

Output

Print one integer: the maximum total number of movies.

Constraints
1≤k≤n≤2⋅105
1≤a<b≤109
Example

Input:
5 2
1 5
8 10
3 6
2 5
6 9

Output:
4
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

    n, k = list(map(int, input().split()))
    intervals = []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        intervals.append([a, b])

    print(min(longest_non_overlap(intervals) + k, len(intervals)))
