"""
You are given an array containing n integers.
Your task is to determine the longest increasing subsequence in the array,
i.e., the longest subsequence where every element is larger than the previous one.

A subsequence is a sequence that can be derived from the array by deleting some elements
without changing the order of the remaining elements.

Input

The first line contains an integer n: the size of the array.

After this there are n integers x1,x2,…,xn: the contents of the array.

Output

Print the length of the longest increasing subsequence.

Constraints
1≤n≤2⋅105
1≤xi≤109
Example

Input:
8
7 3 5 3 6 2 9 8

Output:
4
"""
import bisect

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    sorted_list = []
    for v in A:
        idx = bisect.bisect_left(sorted_list, v)
        if idx == len(sorted_list):
            sorted_list.append(v)
        else:
            sorted_list[idx] = v
    print(len(sorted_list))


