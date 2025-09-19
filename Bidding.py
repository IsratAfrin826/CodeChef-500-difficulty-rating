T = int(input())

for _ in range(T):

    A, B, C = map(int, input().split())

    if A > B and A > C:

        print("ALICE")

    elif B > A and B > C:

        print("BOB")

    else:

        print("CHARLIE")