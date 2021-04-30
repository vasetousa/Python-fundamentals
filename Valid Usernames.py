username = input().split(", ")

for name in username:
    if len(name) in range(3, 17):
        if name.isalnum():
            print(name)
        elif name.isalpha():
            print(name)
        elif name.isdigit():
            print(name)
        elif "-" in name or "_" in name:
            print(name)