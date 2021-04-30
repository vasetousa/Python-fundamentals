def find_evens():
    integer = []
    list_evens = []
    for k in list_integer_array:
        integer.append(int(k))
        if k % 2 == 0:
            list_evens.append(k)
    if len(list_evens) == 0:
        list_evens = 0
        return list_evens
    return list_evens


def find_odds():
    integer = []
    list_odds = []
    for j in list_integer_array:
        integer.append(int(j))
        if j % 2 != 0:
            list_odds.append(j)
    if len(list_odds) == 0:
        list_odds = 0
        return list_odds
    return list_odds

def get_mostright_index_odd():

    index_func = 0
    replacement_number = 100000
    replacement_list = list_integer_array
    counter = 0      # counter for the number of instances, so it does not replace all. last one must stay.
    result = replacement_list.count(minimum)  # count the number of min_odd in list
    if result > 1:
        for n, h in enumerate(replacement_list):
            if h == minimum:
                replacement_list[n] = replacement_number
                counter += 1
                if counter == result - 1:
                    break
    for h in replacement_list:
        index_func = replacement_list.index(h)
        if h == minimum:
            original = return_list_to_original_state()     # must return the list_integer_array to previous state.
            break
    return index_func

def get_mostright_index_even():

    index_func = 0
    replacement_number = 100000
    replacement_list = list_integer_array
    counter = 0     # counter for the number of instances, so it does not replace all. last one must stay.
    result = replacement_list.count(minimum)  # count the number of min_odd in list
    if result > 1:
        for n, d in enumerate(replacement_list):
            if d == minimum:
                replacement_list[n] = replacement_number
                counter += 1
                if counter == result - 1:
                    break
    for g in replacement_list:
        index_func = replacement_list.index(g)
        if g == minimum:
            original = return_list_to_original_state()     # must return the list_integer_array to previous state.
            break
    return index_func

def return_list_to_original_state():
    if minimum == 0:
        repl_number = minimum
    else:
        repl_number = minimum
    repl_list = list_integer_array
    counter = 0  # counter for the number of instances, so it does not replace all. last one must stay.
    result2 = repl_list.count(100000)  # count the number of min_odd in list
    if result2 > 0:
        for r, e in enumerate(repl_list):
            if e == 100000:
                repl_list[r] = repl_number
                counter += 1
                if counter == result2:
                    break
        return

array_to_manipulate = input().split(" ")
list_commands = []
list_integer_array = []
minimum = 0
is_end = False
command_counter = 1
# create a list with integers from the list of elements
for i in array_to_manipulate:
    list_integer_array.append(int(i))

command = input().split(" ")
list_commands = [command[0]]
while command[0] != "end":

    # command "exchange (int)"
    if command[0] == "exchange":
        integer_command = int(command[1])  # take the integer after the command
        if integer_command > len(list_integer_array) or integer_command < 0:
            print("Invalid index")
            command = input().split(" ")
            continue
        exchange_slice_part1_of_list = array_to_manipulate[:integer_command + 1]
        exchange_slice_part2_of_list = array_to_manipulate[integer_command + 1:]
        #       array_to_manipulate = array_to_manipulate[integer_command:]
        array_to_manipulate = exchange_slice_part2_of_list + exchange_slice_part1_of_list
        list_integer_array.clear()

        # create a list with integers from the list of elements
        for i in array_to_manipulate:
            list_integer_array.append(int(i))
#        print(list_integer_array)                   # delete
    # finding the min/max even/odds
    elif command[0] == "max":
        if command[1] == "even":
            result_even = find_evens()
            if result_even != 0:
                minimum = max(result_even)
                index = 0
                count = list_integer_array.count(minimum)  # checks for more than 1 instances in the list
                if count <= 1:
                    for t in list_integer_array:
                        if t == minimum:
                            index = list_integer_array.index(t)
                    print(index)
                else:
                    get_index = get_mostright_index_even()
                    print(get_index)
            else:
                print("No matches")

        elif command[1] == "odd":
            result_odd = find_odds()                    # first to create the odds list
            if result_odd != 0:
                minimum = max(result_odd)
                index = 0
                count = list_integer_array.count(minimum)  # checks for more than 1 instances in the list
                if count <= 1:
                    for t in list_integer_array:
                        if t == minimum:
                            index = list_integer_array.index(t)
                    print(index)
                else:
                    get_index = get_mostright_index_odd()
                    print(get_index)
            else:
                print("No matches")

    elif command[0] == "min":
        if command[1] == "even":
            result_even = find_evens()
            if result_even != 0:
                minimum = min(result_even)
                index = 0
                count = list_integer_array.count(minimum)  # checks for more than 1 instances in the list
                if count <= 1:
                    for t in list_integer_array:
                        if t == minimum:
                            index = list_integer_array.index(t)
                    print(index)
                else:
                    get_index = get_mostright_index_even()
                    print(get_index)
            else:
                print("No matches")

        elif command[1] == "odd":
            result_odd = find_odds()
            if result_odd != 0:
                minimum = min(result_odd)
                index = 0
                count = list_integer_array.count(minimum)    # checks for more than 1 instances in the list
                if count <= 1:
                    for t in list_integer_array:
                        if t == minimum:
                            index = list_integer_array.index(t)
                    print(index)
                else:
                    get_index = get_mostright_index_odd()
                    print(get_index)
            else:
                print("No matches")

#     finding the first even/odds
    elif command[0] == "first":
        if command[2] == "even":
            integer_command = int(command[1])
            result_even = find_evens()                           # list with evens
            if integer_command > len(list_integer_array):
                print("Invalid count")
            else:
                if result_even != 0:
                    f_even = result_even[:integer_command]      # getting the first "n" evens from the command
                    print(f_even)
                else:
                    print("[]")
        elif command[2] == "odd":
            result_odd = find_odds()  # list with odds
            integer_command = int(command[1])
            if integer_command > len(list_integer_array):
                print("Invalid count")
            else:
                if result_odd != 0:
                    f_odd = result_odd[:integer_command]        # getting the first "n" odds from the command
                    print(f_odd)
                else:
                    print("[]")
    # finding the last even/odds
    elif command[0] == "last":
        if command[2] == "even":
            integer_command = int(command[1])
            result_even = find_evens()  # list with evens
            if integer_command > len(list_integer_array):
                print("Invalid count")
            else:
                if result_even != 0:
                    f_even = result_even[-integer_command:]  # getting the last "n" evens from the command
                    print(f_even)
                else:
                    print("[]")
        elif command[2] == "odd":
            integer_command = int(command[1])
            result_odd = find_odds()                        # list with odds
            if integer_command > len(list_integer_array):
                print("Invalid count")
            else:
                if result_odd != 0:
                    f_odd = result_odd[-integer_command:]        # getting the last "n" odds from the command
                    print(f_odd)
                else:
                    print("[]")
    command_counter += 1
    if command_counter == 50:
        break
    command = input().split(" ")
    if command[0] == "end":
        is_end = True

# when command "end", clear the int list, add the new array and print current status
list_integer_array.clear()
for s in array_to_manipulate:
    list_integer_array.append(int(s))
print(list_integer_array)
