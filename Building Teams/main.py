"""
There are n pupils in Uolevi's class, and m friendships between them. Your task is to divide the pupils into two teams
in such a way that no two pupils in a team are friends.
You can freely choose the sizes of the teams.

Input
The first input line has two integers n and m: the number of pupils and friendships. The pupils are numbered 1,2,…,n.

Then, there are m lines describing the friendships. Each line has two integers a and b: pupils a and b are friends.

Every friendship is between two different pupils. You can assume that there is at most one friendship between any two pupils.

Output
Print an example of how to build the teams. For each pupil, print "1" or "2" depending on to which team the pupil will be assigned.
You can print any valid team.

If there are no solutions, print "IMPOSSIBLE".

Constraints
1≤n≤105
1≤m≤2⋅105
1≤a,b≤n
Example

Input:
5 3
1 2
1 3
4 5

Output:
1 2 2 1 2
"""
import collections

if __name__ == '__main__':
    def fn(n: int):
        colors = [None] * n
        for i in range(n):
            if colors[i] is None:
                st = [i]
                colors[i] = 1
                while st:
                    v = st.pop()
                    for u in graph[v]:
                        if colors[u] is None:
                            colors[u] = colors[v] ^ 1
                            st.append(u)
                        elif colors[u] == colors[v]:
                            return None
        return colors


    n, m = list(map(int, input().split()))
    graph = collections.defaultdict(list)

    for _ in range(m):
        a, b = list(map(int, input().split()))
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    colors = fn(n)

    if not colors:
        print("IMPOSSIBLE")
    else:
        print(*['1' if c == 1 else '2' for c in colors])
