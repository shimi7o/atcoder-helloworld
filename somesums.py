n, a, b = map(int, input().split())

count = 0

for i in range(1, n+1):
    if a <= sum(list(map(int, str(i)))) <= b:
        count += i

print(count)
