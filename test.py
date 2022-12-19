coins = [500, 100, 50, 10, 5, 1]
count = 0

cost = int(input())
change = 1000 - cost

for coin in coins:
    count += change // coin
    change %= coin

print(count)
