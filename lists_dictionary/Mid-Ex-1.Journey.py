journey_cost = float(input())
months = int(input())
budged = 0
current_money = 0
for month in range(1, months+1):
    if month > 1:
        if month % 2 != 0:      # every odd month spending 16% of savings so far (budged)
            budged = budged - (budged * 0.16)
    if month % 4 == 0:      # every 4rth month + 25% bonus from savings so far (budged)
        budged = budged + (budged * 0.25)
    current_money = journey_cost * 0.25
    budged += current_money
if budged >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {budged - journey_cost:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {journey_cost - budged:.2f}lv. more.")