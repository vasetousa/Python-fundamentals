import re
data = input()     # function
food_to_eat = []
pattern = r"(#|\|)(?P<name>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<cal>[0-9][0-9]{0,3}|10000)\1"
total_calories = 0

matched_items = [obj.groupdict() for obj in re.finditer(pattern, data)]


for key in matched_items:
    total_calories += int(key['cal'])
days_to_last = total_calories // 2000

print(f"You have food to last you for: {days_to_last} days!")

for el in matched_items:
    print(f"Item: {el['name']}, Best before: {el['date']}, Nutrition: {el['cal']}")


#  #Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|
#  $$#@@%^&#Fish#24/12/20#8500#|#Incorrect#19.03.20#450|$5*(@!#Ice Cream#03/10/21#9000#^#@aswe|Milk|05/09/20|2000|
#  Hello|#Invalid food#19/03/20#450|$5*(@


