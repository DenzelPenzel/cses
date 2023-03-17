"""
You are in a book shop which sells n different books.

You know the price and number of pages of each book.

You have decided that the total price of your purchases will be at most x.

What is the maximum number of pages you can buy? You can buy each book at most once.

Input

The first input line contains two integers n and x: the number of books and the maximum total price.

The next line contains n integers h1,h2,…,hn: the price of each book.

The last line contains n integers s1,s2,…,sn: the number of pages of each book.

Output

Print one integer: the maximum number of pages.

Constraints
    1≤n≤1000
    1≤x≤105
    1≤hi,si≤1000
Example

Input:
4 10
4 8 5 3
5 12 8 1

Output:
13

Explanation: You can buy books 1 and 3. Their price is 4+5=9 and the number of pages is 5+8=13.

"""
if __name__ == '__main__':
    n, target = list(map(int, input().split()))
    price = list(map(int, input().split()))
    pages = list(map(int, input().split()))
    dp = [0] * (target + 1)
    for coin, page in sorted([(x, y) for x, y in zip(price, pages)], key=lambda x: x[0]):
        if coin > target: break
        for w in range(target, coin - 1, -1):
            dp[w] = max(dp[w], dp[w - coin] + page)
    print(dp[target])
