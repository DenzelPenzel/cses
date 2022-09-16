from typing import List

if __name__ == '__main__':
    def longest_non_overlap(A: List[List[int]]) -> List[List[int]]:
        A.sort(key=lambda x: x[0])
        prev = None
        cnt = 0
        for i in range(len(A)):
            if prev is None or prev <= A[i][0]:
                prev = A[i][1]
                cnt += 1
            else:
                prev = min(prev, A[i][1])
        return len(A) - cnt

    n = list(map(int, input().split()))[0]
    intervals = []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        intervals.append([a, b])

    print(len(intervals) - longest_non_overlap(intervals))
