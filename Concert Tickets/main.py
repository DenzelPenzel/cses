"""
There are n concert tickets available, each with a certain price. Then, m customers arrive, one after another.

Each customer announces the maximum price they are willing to pay for a ticket, and after this,
they will get a ticket with the nearest possible price such that it does not exceed the maximum price.

Input

The first input line contains integers n and m: the number of tickets and the number of customers.

The next line contains n integers h1,h2,…,hn: the price of each ticket.

The last line contains m integers t1,t2,…,tm: the maximum price for each customer in the order they arrive.

Output

Print, for each customer, the price that they will pay for their ticket. After this, the ticket cannot be purchased again.

If a customer cannot get any ticket, print −1.

Constraints
1≤n,m≤2⋅105
1≤hi,ti≤109
Example

Input:
5 3
5 3 7 8 5
4 8 3

Output:
3
8
-1
"""
import bisect

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    ticket_prices = list(sorted(map(int, input().split())))
    user_price = list(map(int, input().split()))

    for x in user_price:
        if not ticket_prices:
            print(-1)
        else:
            idx = bisect.bisect_left(ticket_prices, x)
            if (idx == 0 and ticket_prices[idx] > x):
                print(-1)
            else:
                if idx < len(ticket_prices) and ticket_prices[idx] == x:
                    print(ticket_prices[idx])
                    del ticket_prices[idx]
                else:
                    print(ticket_prices[idx - 1])
                    del ticket_prices[idx - 1]
