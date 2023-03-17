"""
Given a string, your task is to generate all different strings that can be created using its characters.

Input

The only input line has a string of length n. Each character is between a–z.

Output

First print an integer k: the number of strings. Then print k lines: the strings in alphabetical order.

Constraints
1≤n≤8
Example

Input:
aabac

Output:
20
aaabc
aaacb
aabac
aabca
aacab
aacba
abaac
abaca
abcaa
acaab
acaba
acbaa
baaac
baaca
bacaa
bcaaa
caaab
caaba
cabaa
cbaaa
"""
import collections

if __name__ == '__main__':
    x = list(sorted(input()))
    ans = []
    def DFS(path, counter):
        if len(path) == len(x):
            ans.append(("".join(path)))
            return
        for k in counter:
            if counter[k]:
              path.append(k)
              counter[k] -= 1
              DFS(path, counter)
              path.pop()
              counter[k] += 1
    DFS([], collections.Counter(x))
    print(len(ans))
    print(*ans)