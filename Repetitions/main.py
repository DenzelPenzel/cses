"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T. 
Your task is to find the longest repetition in the sequence. 
This is a maximum-length substring containing only one type of character.

Input

The only input line contains a string of n characters.

Output

Print one integer: the length of the longest repetition.

Constraints
1≤n≤106
Example

Input:
ATTCGGGA

Output:
3
"""

if __name__ == '__main__':
    s = input()
    cnt = res = 0
    curr = ''
    for ch in s:
        if not curr:
            curr = ch
        if ch == curr:
            cnt += 1
        else:
            res = max(res, cnt)
            cnt = 1
            curr = ch

    print(max(res, cnt))
