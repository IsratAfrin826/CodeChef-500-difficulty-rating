T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())

    investment = X - Y

    print(investment)