"""
Consider a game where there are n children (numbered 1,2,…,n) in a circle.
During the game, every second child is removed from the circle, until there are no children left.

In which order will the children be removed?

Input

The only input line has an integer n.

Output

Print n integers: the removal order.

Constraints
1≤n≤2⋅105
Example

Input:
7

Output:
2 4 6 1 5 3 7
"""
import collections
from collections import OrderedDict
from typing import List

if __name__ == '__main__':
    def test_II(n: int) -> List[int]:
        if n == 1:
            return [1]

        mapping = OrderedDict()

        for i in range(1, n + 1):
            mapping[i] = i

        res = []
        k = 2
        while mapping:
            if res:
                keys = list(mapping.keys())
                # get the next initial number
                start = keys[1] if (res[-1] > keys[-1] and len(mapping) > 1) else keys[0]
            else:
                start = 2

            mapping[start] = True

            while start <= n + 1 and start in mapping:
                res.append(start)
                del mapping[start]
                start += k
            k *= 2
        return res


    def test(n: int) -> List[int]:
        res = []
        queue = collections.deque(list(range(1, n + 1)))
        while len(queue) >= 2:
            x = queue.popleft()
            res.append(queue.popleft())
            queue.append(x)
        res.append(queue.popleft())
        return res


    n = int(input())
    print(*test(n))
