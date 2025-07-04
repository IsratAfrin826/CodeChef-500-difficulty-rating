T = int(input())

for _ in range(T):
    X, y = map(int, input().split())

    price_top_10 = 10 * X

    price_top_90 = 90 * y

    total_price = price_top_10 + price_top_90

    print(total_price)