import math
party_size = int(input())
days_of_party = int(input())

coins = 0

for i in range(1, days_of_party+1):

    if i % 10 == 0:
        party_size -= 2
    if i % 15 == 0:
        party_size += 5

    coins += 50 - (party_size * 2)  # coins per day minus food

    if i % 3 == 0:
        coins -= (party_size * 3)
    if i % 5 == 0:
        coins += (party_size * 20)
    if i % 3 == 0 and i % 5 == 0:
        coins -= (party_size * 2)

coins = coins / party_size
total_coins = math.floor(coins)
print(f"{party_size} companions received {total_coins} coins each.")