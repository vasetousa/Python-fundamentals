def password_check(word):
    is_valid = False
    digit = 0
    is_wrong_char = False
    is_between_6_10 = False

    if 6 <= len(word) <= 10:
        is_between_6_10 = True
    # ASCII num - 48-57; abc - 97-122; ABC - 65-90
    for index in word:
        el = ord(index)
        if el < 48:
            is_wrong_char = True
        if 57 < el < 65:
            is_wrong_char = True
        if el > 122:
            is_wrong_char = True
        if 90 < el < 97:
            is_wrong_char = True
        if 48 <= el <= 57:
            digit += 1

    #       6-10,         2 digits,     right chars
    #       true            true            true    VALID PASSWORD
    #       true            true            false   *   login12$ 6,1,false
    #       true            false            true   *   login1  6,1,true
    #       true            false            false   *  login1$
    #       false           true             true    *  l12    3,2,true
    #       false           true             false   *  l12$   4,2,false
    #       false           false            true    *  l1k    3,1,true
    #       false           false            false   *  l1$    3,1,false

    if is_between_6_10 and digit >= 2 and is_wrong_char:
        print("Password must consist only of letters and digits")

    if is_between_6_10 and digit < 2 and is_wrong_char:
        print("Password must consist only of letters and digits")
        print("Password must have at least 2 digits")
    if is_between_6_10 and digit < 2 and not is_wrong_char:
        print("Password must have at least 2 digits")
    if not is_between_6_10 and digit >= 2 and is_wrong_char:
        print("Password must be between 6 and 10 characters")
        print("Password must consist only of letters and digits")
    if not is_between_6_10 and digit >= 2 and not is_wrong_char:
        print("Password must be between 6 and 10 characters")
    if not is_between_6_10 and digit < 2 and is_wrong_char:
        print("Password must be between 6 and 10 characters")
        print("Password must have at least 2 digits")
        print("Password must consist only of letters and digits")
    if not is_between_6_10 and digit < 2 and not is_wrong_char:
        print("Password must be between 6 and 10 characters")
        print("Password must have at least 2 digits")
    if is_between_6_10 and digit >= 2 and not is_wrong_char:
        print("Password is valid")


password = input()
result = password_check(password)