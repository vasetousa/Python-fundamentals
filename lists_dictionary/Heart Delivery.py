houses = [int(el) for el in input().split("@")]
index_house = 0
len_houses = len(houses)
zero_houses = houses.count(0)       # if any zeros in the list
command = input().split(" ")
jump_counter = 0
while command[0] != "Love!":
    if command[0] == "Jump":
        length_2 = command[1]               # Jump "length_2" positions
        jump_counter += int(length_2)
        if int(length_2) >= len_houses:      # if the Jump value "length_2" > list length "len_houses"
            index_house = 0
            jump_counter = 0
            length_2 = '0'
        index_house += int(length_2)
        if jump_counter >= len_houses:
            index_house = 0
            jump_counter = 0
        if houses[index_house] == 0:
            print(f"Place {index_house} already had Valentine's day.")
        else:
            houses[index_house] -= 2
            if houses[index_house] == 0:
                print(f"Place {index_house} has Valentine's day.")
    command = input().split()
house_count = houses.count(0)
h_counter = len_houses - house_count - zero_houses
print(f"Cupid's last position was {index_house}.")
if house_count == len_houses:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {h_counter} places.")


#   2@2@2@2@2@2@2@2@2@2 Jump 11 Jump 5 Jump 3 Jump 8 Jump 10 Jump 3 Jump 2 Love!
#    0@0@0 1 2