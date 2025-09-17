T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())

    max_attacks = Y // X

    print(max_attacks)