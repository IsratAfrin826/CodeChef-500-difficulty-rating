T = int(input())

for _ in range(T):

    X, Y = map(int, input().split())

    if X >= Y:

        print("Yes")

    else:

        print("No")