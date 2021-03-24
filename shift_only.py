n = int(input())
numbers = list(map(int, input().split()))

count = 0

while all(number % 2 == 0 for number in numbers):
    numbers = [number // 2 for number in numbers]
    count += 1

print(count)

# def hoge(numbers, count):
#     new_numbers = []

#     for number in numbers:
#         if number % 2 != 0:
#             return count
#         new_numbers.append(number // 2)

#     return hoge(new_numbers, count+1)


# print(hoge(numbers, 0))


# count = 0
# flag = False

# while True:
#     for i, number in enumerate(numbers):
#         if number % 2 != 0:
#             flag = True
#             break
#         numbers[i] = number // 2
#     if flag:
#         break
#     count += 1

# print(count)
