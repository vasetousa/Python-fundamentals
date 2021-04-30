command = input()
todo_list = [0] * 10

while command != "End":
    importance, task = command.split("-")   # 2 variables - example -> 2, Walk the dog
    importance = int(importance) - 1    # int from the variable 2
    todo_list[importance] = task

    command = input()
print([task for task in todo_list if not task == 0])


# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# 5-Work
# 7-Drop a turd
# 3-Watch some TV
# 4-Take a shower
# 8-Go sleep with the neighbor's wife
# End