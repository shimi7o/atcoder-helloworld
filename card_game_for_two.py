n = int(input())
cards = list(map(int, input().split()))

cards.sort(reverse=True)
print(sum(cards[::2])-sum(cards[1::2]))

# alice_score = 0
# bob_score = 0

# while True:
#     if len(cards) == 0:
#         break

#     a = max(cards)
#     alice_score += a
#     del cards[cards.index(a)]

#     if len(cards) == 0:
#         break

#     b = max(cards)
#     bob_score += b
#     del cards[cards.index(b)]

# print(alice_score-bob_score)
