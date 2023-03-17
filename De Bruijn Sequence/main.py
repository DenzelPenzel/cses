"""
Your task is to construct a minimum-length bit string that contains all possible substrings of length n.
For example, when n=2, the string 00110 is a valid solution, because its substrings of length 2 are 00, 01, 10 and 11.

Input

The only input line has an integer n.

Output

Print a minimum-length bit string that contains all substrings of length n.
You can print any valid solution.

Constraints
1≤n≤15

Example

Input:
2

Output:
00110
"""
import collections
import sys

from collections import defaultdict
from itertools import product

sys.setrecursionlimit(10 ** 6)

graph = defaultdict(list)
mp = defaultdict(int)
mp2 = defaultdict(str)
index = 0


def generate_substrings(s, n):
    global index
    if len(s) == n - 1:
        index += 1
        mp[s] = index
        mp2[index] = s
        return
    generate_substrings(s + '0', n)
    generate_substrings(s + '1', n)


"""
The idea of the code is to create a de Bruijn graph, 
which is a directed graph that represents overlapping substrings of a given length.
 
However, not all de Bruijn graphs represent valid solutions to the problem!

To generate a valid solution, it is necessary to ensure that the de Bruijn graph is acyclic. 
"""
if __name__ == "__main__":
    n = int(input())

    if n == 1:
        print("01")
        exit(0)

    generate_substrings("", n)

    for v in range(1, 1 << n):
        x = mp2[v][1:n - 1]
        graph[v].append((mp[x + '0'], '0'))
        graph[v].append((mp[x + '1'], '1'))

    # Eulerian path always exists
    path = ""
    st = [(1, '#')]

    while st:
        i, c = st[-1]
        if not graph[i]:
            if c != '#':
                path += c
            st.pop()
        else:
            j, c2 = graph[i].pop()
            st.append((j, c2))

    print(path + mp2[1])
