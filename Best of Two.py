T = int(input())

for _ in range(T):
    X, y = map(int, input().split())

    print(max(X, y))