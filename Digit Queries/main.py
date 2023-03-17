"""
Consider an infinite string that consists of all positive integers in increasing order:

12345678910111213141516171819202122232425...

Your task is to process q queries of the form: what is the digit at position k in the string?

Input

The first input line has an integer q: the number of queries.

After this, there are q lines that describe the queries. Each line has an integer k: a 1-indexed position in the string.

Output

For each query, print the corresponding digit.

Constraints
1≤q≤1000
1≤k≤1018
Example

Input:
3
7
19
12

Output:
7
4
1

====================================

1 - [1 - 9]
2 - [10 - 189] [10 - 99]
3 - [190 - 2890] [100 - 999]

1 = 9
2 = 180 => (100 - 10) * 2 = 180
3 = 2700 => (1000 - 100) * 3 = 2700

107 => 58 => 8

"""

if __name__ == '__main__':
    def search(target_idx: int) -> str:
        if target_idx < 10:
            return str(target_idx)
        else:
            d = 90
            digit_len = 2
            start = 10
            before = 10
            while True:
                end = d * digit_len + start
                if start <= target_idx < end: break
                before += end - start
                start = end
                d *= 10
                digit_len += 1

            left_boundary = 10 ** (digit_len - 1)
            right_boundary = (10 ** digit_len) - 1
            start, end = left_boundary, right_boundary
            best_val = 0
            best_val_idx = None

            # binary search to find the best num in the range (10 << x << 99)
            while start <= end:
                num = start + ((end - start) >> 1)
                idx = before + (num - left_boundary) * digit_len  # calc index for the `num`
                if idx <= target_idx:
                    if num > best_val:
                        best_val = num
                        best_val_idx = idx
                    start = num + 1
                else:
                    end = num - 1
            return str(best_val)[target_idx - best_val_idx]
    n = int(input())
    res = []
    for _ in range(n):
        k = int(input())
        res.append(search(k))
    print(*res)
