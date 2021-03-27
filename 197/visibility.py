H, W, X, Y = map(int, input().split())

S = []
for i in range(H):
    array = list(input())
    S.append(array)

count = 0

for n in range(Y, W):
    if S[X-1][n] == "#":
        break

    if S[X-1][n] == ".":
        count += 1

for n in range(Y-2, -1, -1):
    if S[X-1][n] == "#":
        break

    if S[X-1][n] == ".":
        count += 1

for n in range(X, H):
    if S[n][Y-1] == "#":
        break

    if S[n][Y-1] == ".":
        count += 1

for n in range(X-2, -1, -1):
    if S[n][Y-1] == "#":
        break

    if S[n][Y-1] == ".":
        count += 1


print(count+1)
