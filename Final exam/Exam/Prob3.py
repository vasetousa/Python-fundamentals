data = input()
info_distributors = {}
info_clients = {}

while not data == "End":
    command, name, cost = data.split()
    cost = float(cost)
    if command == "Deliver":
        if name not in info_distributors:
            info_distributors[name] = cost
        else:
            info_distributors[name] += cost
    elif command == "Return":
        if name in info_distributors:
            if not info_distributors[name] < cost:
                info_distributors[name] -= cost
                if info_distributors[name] <= 0:
                    del info_distributors[name]


    elif command == "Sell":
        if name not in info_clients:
            money_spend = cost
            info_clients[name] = money_spend
        else:
            money_spend = cost
            info_clients[name] += money_spend



    data = input()
total_money_spend = 0
for key, value in info_clients.items():
    total_money_spend += value

sorted_clients = sorted(info_clients.items(), key=lambda kvp: kvp[0])
sorted_distributors = sorted(info_distributors.items(), key=lambda kvp: kvp[0])

for key, value in sorted_clients:
    print(f'{key}: {value:.2f}')
print("-----------")
for key, value in sorted_distributors:
    print(f'{key}: {value:.2f}')
print("-----------")
print(f"Total Income: {total_money_spend:.2f}")
