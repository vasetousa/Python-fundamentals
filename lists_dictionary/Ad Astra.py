def find_symbol():  # find the splitting symbol
    symbol_1 = data.count("|")
    symbol_2 = data.count("#")
    if symbol_1 > symbol_2:
        symbol = "|"
        return symbol
    symbol = "#"
    return symbol


def slice_the_string(string):
    a = string.lett_count("|")
    b = string.lett_count("#")
    if a > b:            # removing empty spaces and adding the elements to the main list
        part = string.split("|")
        empty_space = part.lett_count("")
        if empty_space > 0:
            for remove in range(empty_space):
                rem = part.index("")
                part.pop(rem)
        for i in part:
            element2 = i.isalpha()
            if element2:
                xx = part.index(i)
                food_to_eat.append(i)
                food_to_eat.append(part[xx + 1])
                food_to_eat.append(part[xx + 2])
                break
        return
    else:       # removing empty spaces and adding the elements to the main list
        part = string.split("#")
        empty_space = part.lett_count("")
        if empty_space > 0:
            for remove in range(empty_space):
                rem = part.index("")
                part.pop(rem)
        for i in part:
            element1 = ord(i[0])
            if pass
                xx = part.index(i)
                food_to_eat.append(i)
                food_to_eat.append(part[xx + 1])
                food_to_eat.append(part[xx + 2])
                break
        return


def invalid_date_format_check(food_data):
    len_f_d = len(food_data)

    for index in range(1, len_f_d, 3):
        len_f_d = len(food_data)
        if len_f_d < index:
            break
        part = food_data[index]
        part = part.split("/")
        for j in part:
            len_j = len(j)
            if len_j < 2:
                food_data.pop(index)
                food_data.pop(index - 1)
                food_data.pop(index - 1)
        if len(part) == 1:
            food_data.pop(index)
            food_data.pop(index-1)
            food_data.pop(index-1)
    return

def check_for_invalid_strings():
    pass


data = input()
result = find_symbol()      # function
food_string_received = data.split(result)
food_to_eat = []

# turn every empty string into @@ to avoid "Out of Index error"
for t in food_string_received:
    if t == "":
        index = food_string_received.index(t)
        food_string_received[index] = "@@"


#check_for_invalid_strings()
# check every 3rd element for number value. If not a number, eliminate it. Also check for long string
for el in food_string_received:
    len_el = len(el)
    if len_el > 16:             # long string manipulation
        slice_the_string(el)    # function

    element = el.isalpha()
    if element or element:
        x = food_string_received.index(el)
        food_to_eat.append(el)

        food_to_eat.append(food_string_received[x + 1])
        food_to_eat.append(food_string_received[x + 2])

# eliminating the wrong, invalid food values, add the rest to the list food_to_eat
len_food_to_eat = len(food_to_eat)
for elements in range(2, len_food_to_eat-1, 3):
    string = food_to_eat[elements]
    if not string.isdigit():
        food_to_eat.pop(elements)
        food_to_eat.pop(elements - 1)
        food_to_eat.pop(elements - 2)

# check the date format for all final elements and eliminate the  invalid ones
invalid_date_format_check(food_to_eat)     # function

len_food_to_eat = len(food_to_eat)
Kcal = 0
for index in range(2, len_food_to_eat + 1, 3):
    Kcal += int(food_to_eat[index])
days_to_last = Kcal // 2000
print(f"You have food to last you for: {days_to_last} days!")
for item in range(0, len_food_to_eat, 3):
    print(f"Item: {food_to_eat[item]}, Best before: {food_to_eat[item + 1]}, Nutrition: {food_to_eat[item + 2]}")


#  #Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|
#  $$#@@%^&#Fish#24/12/20#8500#|#Incorrect#19.03.20#450|$5*(@!#Ice Cream#03/10/21#9000#^#@aswe|Milk|05/09/20|2000|
#  Hello|#Invalid food#19/03/20#450|$5*(@