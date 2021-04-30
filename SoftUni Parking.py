n = int(input())   # number of commands
commands = {}
for el in range(n):
    command = input().split()
    username = command[1]
    if command[0] == 'register':
        plate = command[2]
        if username not in commands:
            commands[username] = plate
            print(f"{username} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    elif command[0] == 'unregister':
        if username not in commands:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del commands[username]

for username, plate in commands.copy().items():
    print(f"{username} => {plate}")