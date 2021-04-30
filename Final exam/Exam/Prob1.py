text = input()  # user password
leng = len(text)
is_found = False

command = input()
while not command == "Complete":
    try:
        if command.startswith("Make Upper"):
            action, action2, index = command.split()
            index = int(index)
            x = text[index]
            z = x.upper()
            y = text.replace(x, z) # TODO re-work this portion with "for cycle", to replace only 1 letter, not all
            text = y
            print(text)
        elif command.startswith("Make Lower"):
            action, action2, index = command.split()
            index = int(index)
            x = text[index]
            z = x.lower()
            y = text.replace(x, z)
            text = y
            print(y)
        elif command.startswith("Insert"):
            action, index, char = command.split()
            index = int(index)
            start = text[:index]
            end = text[index:]
            all = start+char+end
            text = all
            print(text)
        elif command.startswith("Replace"):
            action, char, value = command.split()
            if char in text:
                value = int(value)
                code = ord(char) + value      # get the ASCII and sum with value
                new_char = chr(code)
                x = text.replace(char, new_char)
                text = x
                print(text)
        elif command.startswith("Validation"):
            if leng < 8:
                print("Password must consist at least 8 characters long!")
            if not text.isalnum():
                print("Password must consist only of letters, digits and _!")
            if text.isupper():
                print(f"Password must consist at least one lowercase letter!")
            if text.islower():
                print(f"Password must consist at least one uppercase letter!")
            for el in text:
                if el.isdigit():
                    is_found = True
                    break
            if not is_found:
                print(f"Password must consist at least one digit!")

    except KeyError:
        pass


    command = input()