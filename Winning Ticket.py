def check_ticket(char, string, integer):
    if integer == 20:
        print(f'ticket "{string}" - {integer/2:.0f}{char} Jackpot!')
        return True
    left_part = string[:10]
    right_part = string[10:]
    is_found = False
    left_counter = 0
    right_counter = 0
    for el in left_part:             # 2 "for" cycles to count the symbols in each parts
        if el == char:
            left_counter += 1
            is_found = True
        else:
            if is_found:
                break
    is_found = False
    for el in right_part:
        if el == char:
            right_counter += 1
            is_found = True
        else:
            if is_found:
                break
    mina = min(left_counter, right_counter)
    if left_counter in range(6, 11) and right_counter in range(6, 11):
        print(f'ticket "{string}" - {mina}{char}')
        return True
    return False


tickets = [el.strip() for el in input().split(", ")]
symbol = ''
for el in tickets:
    result = False
    len_el = len(el)
    if len_el == 20:
        kliomba = el.count("@")
        dollar = el.count("$")
        ogradka = el.count("#")
        kyshta = el.count("^")
        digit = max(kliomba, dollar, ogradka, kyshta)
        if kliomba in range(12, 21):
            symbol = "@"
            result = check_ticket(symbol, el, digit)
        elif dollar in range(12, 21):
            symbol = "$"
            result = check_ticket(symbol, el, digit)
        elif ogradka in range(12, 21):
            symbol = "#"
            result = check_ticket(symbol, el, digit)
        elif kyshta in range(12, 21):
            symbol = "^"
            result = check_ticket(symbol, el, digit)
        if not result:
            print(f'ticket "{el}" - no match')
    else:
        print("invalid ticket")