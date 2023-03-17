"""
There are n people who want to get to the top of a building which has only one elevator.

You know the weight of each person and the maximum allowed weight in the elevator.

What is the minimum number of elevator rides?

Input:

The first input line has two integers n and x: the number of people and the maximum allowed weight in the elevator.

The second line has n integers w1,w2,…,wn: the weight of each person.

Output:
Print one integer: the minimum number of rides.

Constraints:
1≤n≤20
1≤x≤109
1≤wi≤x
Example

Input:
4 10
4 8 6 1

Output:
2
"""

if __name__ == '__main__':
    n, max_weight = list(map(int, input().split()))
    A = list(map(int, input().split()))
    if any(x > max_weight for x in A):
        print(0)
    else:
        # Time O(N*2^N)
        state = {0: (0, 0)}  # cnt_steps, weight

        # Iterate through all subsets
        # Idea: for each subset calc (min_number_of_steps, min_weight)
        # If we have two subsets A and B
        # A ⊂ B because A processed earlier B then DP works in the correct way
        for mask in range(1, 1 << n):
            state[mask] = (n + 1, 0)
            for i in range(n):
                if mask & (1 << i):
                    prev_mask = mask ^ (1 << i)
                    cnt_steps, weight = state[prev_mask]
                    # we can add A[i] in the current subset
                    if weight + A[i] <= max_weight:
                        # increase subset's weight
                        weight += A[i]
                    else:
                        # can't add A[i] in the current subset, need to add into the new subset
                        cnt_steps += 1
                        weight = A[i]
                    # update the current state by taking the best state
                    state[mask] = min(state[mask], (cnt_steps, weight))
        # final answer store in the mask = (1 << n) when all bits == 1 | example 15 => 1111
        print(state[(1 << n) - 1][0] + 1)

