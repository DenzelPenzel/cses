"""
There are n applicants and m free apartments. Your task is to distribute the apartments so that as many applicants as possible will get an apartment.

Each applicant has a desired apartment size, and they will accept any apartment whose size is close enough to the desired size.

Input

The first input line has three integers n, m, and k: the number of applicants, the number of apartments, and the maximum allowed difference.

The next line contains n integers a1,a2,…,an: the desired apartment size of each applicant. If the desired size of an applicant is x, he or she will accept any apartment whose size is between x−k and x+k.

The last line contains m integers b1,b2,…,bm: the size of each apartment.

Output

Print one integer: the number of applicants who will get an apartment.

Constraints
1≤n,m≤2⋅105
0≤k≤109
1≤ai,bi≤109
Example

Input:
4 3 5
60 45 80 60
30 60 75

Output:
2
"""

import collections

if __name__ == '__main__':
    people_cnt, apt, diff = list(map(int, input().split()))
    prefer_size = collections.deque(list(sorted(map(int, input().split()))))
    actual_size = list(sorted(map(int, input().split())))

    res = 0

    for i in range(len(actual_size)):
        while prefer_size and prefer_size[0] + diff < actual_size[i]:
            prefer_size.popleft()

        if not prefer_size:
            break

        if prefer_size[0] - diff <= actual_size[i] <= prefer_size[0] + diff:
            prefer_size.popleft()
            res += 1

    print(res)
