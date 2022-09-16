from utils.read_write_io import IOWrapper
import sys

if __name__ == '__main__':
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

    input = lambda: list(map(int, sys.stdin.readline().rstrip("\n").split(" ")))

    n, t = input()
    A = input()

    lo, hi = 1, int(1e18)
    res = float('inf')

    while lo < hi:
        mid = lo + ((hi - lo) >> 1)
        
        cur_time = 0

        for x in A:
            cur_time += mid // x
            if cur_time >= t:
                break

        if cur_time < t:
            lo = mid + 1
        else:
            hi = mid

    print(lo)
