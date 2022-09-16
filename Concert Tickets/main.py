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