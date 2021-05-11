import self as self


class Dragon:
    def __init__(self):
        self.dragon_list = []
        self.dragon_avg = {}
        self.dragon_color_dict = {}

    def add_dragon(self, color, name, damage, health, armor):
        self.color = color
        self.name = name
        self.damage = damage
        self.health = health
        self.armor = armor
# adding the dragons to the list
        self.dragon_list.append(dragon)
# adding colors -> attributes in dictionary
        if self.color in self.dragon_avg:
            self.dragon_avg[color].update(damage, health, armor)
        else:
            self.dragon_avg[color] = damage, health, armor



n = int(input())  # number of dragons
dragon = Dragon()
for el in range(n):
    color, d_name, d_damage, d_health, d_armor = input().split()
    if d_damage == 'null':
        d_damage = 45
    if d_health == 'null':
        d_health = 250
    if d_armor == 'null':
        d_armor = 10
    d_damage = int(d_damage)
    d_health = int(d_health)
    d_armor = int(d_armor)
    dragon.add_dragon(color, d_name, d_damage, d_health, d_armor)

print()
