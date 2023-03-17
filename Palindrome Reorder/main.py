"""
Given a string, your task is to reorder its letters in such a way that it becomes a palindrome (i.e., it reads the same forwards and backwards).

Input

The only input line has a string of length n consisting of characters A–Z.

Output

Print a palindrome consisting of the characters of the original string. You may print any valid solution.
If there are no solutions, print "NO SOLUTION".

Constraints
1≤n≤106
Example

Input:
AAAACACBA

Output:
AACABACAA
"""

import collections

if __name__ == '__main__':
    freq = collections.Counter(input())
    if not freq:
        print("NO SOLUTION")
    else:
        even = sum(1 for k in freq if freq[k] % 2 != 0)
        if even > 1:
            print("NO SOLUTION")
        else:
            res = ""
            if even:
                for k in freq:
                    if freq[k] % 2 != 0:
                        res = k
                        freq[k] -= 1

            for k in freq:
                x = freq[k] // 2
                res = (k * x) + res + (k * x)

            print(res)
