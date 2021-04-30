class Dragon:
    def __init__(self):
        self.dragon_dict = {}
        self.dragon_avg = {}

    def add_dragon(self, types, name, damage, health, armor):
        self.types = types
        self.name = name
        self.damage = damage
        self.health = health
        self.armor = armor
        if types not in self.dragon_dict:  # checking for the same type(color) dragon
            self.dragon_dict[types] = {name: (damage, health, armor)}
            self.dragon_avg[types] = damage, health, armor

        else:  # if the same type(color) is coming
            if self.name not in self.dragon_dict[types]:  # same type(color), but different name -> add to dict
                self.dragon_dict[types][name] = damage, health, armor
                d = self.dragon_avg[types][0]
                h = self.dragon_avg[types][1]
                a = self.dragon_avg[types][2]
                d += damage
                h += health
                a += armor
                self.dragon_avg[types] = d, h, a

            else:  # same type(color) and same name -> same dragon, rewrite the stats
                self.dragon_dict[types][name] = damage, health, armor

        if el == (n-1):
            for ele in self.dragon_avg:
                lenn = len(self.dragon_dict[ele])
                d = self.dragon_avg[ele][0]
                h = self.dragon_avg[ele][1]
                a = self.dragon_avg[ele][2]
                d /= lenn
                h /= lenn
                a /= lenn
                self.dragon_avg[ele] = d, h, a


    def printing(self):
        # sorting the dragons alphabet
        # sorted_dragons = dict(sorted(self.dragon_dict.items(), key=lambda kvp: kvp[0]))
        # printing final values
        for _ in range(len(self.dragon_avg)):
            key, value = self.dragon_avg.items()
            print(f"{key}::({value[0]:.2f}/{value[1]:.2f}/{value[2]:.2f})")
            # for dragone, values in self.dragon_dict.items():
            #     for dr, val in values.items():
            #         print(f'-{dr} -> damage: {val[0]}, health: {val[1]}, armor: {val[2]}')

            return


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





dragon.printing()