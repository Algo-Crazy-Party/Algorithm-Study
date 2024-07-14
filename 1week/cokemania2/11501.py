t = int(input())
reversed_stock_prices = []


for i in range(t):
    n = int(input())
    reversed_stock_prices.append(list(map(int, input().split()))[::-1])

for i in range(t):
    answer = 0
    max_price = 0
    cart = []
    for stock_price in reversed_stock_prices[i]:
        if stock_price > max_price:
            answer += len(cart) * max_price - sum(cart)
            max_price = stock_price
            cart = []
        else:
            cart.append(stock_price)
    answer += len(cart) * max_price - sum(cart)
    print(answer)
