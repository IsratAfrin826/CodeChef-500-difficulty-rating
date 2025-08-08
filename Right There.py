T = int(input())

for _ in range(T):

    N, X = map(int, input().split())

    if N <= X:

        print("YES")

    else:

        print("NO")