"""
You are given a playlist of a radio station since its establishment. The playlist has a total of n songs.

What is the longest sequence of successive songs where each song is unique?

Input

The first input line contains an integer n: the number of songs.

The next line has n integers k1,k2,…,kn: the id number of each song.

Output

Print the length of the longest sequence of unique songs.

Constraints
1≤n≤2⋅105
1≤ki≤109
Example

Input:
8
1 2 1 3 2 7 4 2

Output:
5
"""

from bisect import bisect_left

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    
    counter = {}
    i, j = 0, 0
    res = 0

    while j < len(A):
        counter[A[j]] = counter.get(A[j], 0) + 1 
        while i < j and counter[A[j]] > 1:
            counter[A[i]] -= 1
            i += 1
        res = max(res, j - i + 1)
        j += 1
    
    print(res)