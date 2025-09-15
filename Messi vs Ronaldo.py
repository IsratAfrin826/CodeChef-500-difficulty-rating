A, B, X, Y = map(int, input().split())

messi_points = A * 2 + B

Ronaldo_points = X * 2 + Y

if messi_points > Ronaldo_points:

    print("Messi")

elif messi_points < Ronaldo_points:

    print("Ronaldo")

else:

    print("Equal")